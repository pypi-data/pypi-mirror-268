from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from robot.api.deco import keyword, not_keyword
import json

class Classroom:
    def __init__(self):
        self.creds=None
    
    @keyword("Set Up Classroom Connection")
    def authenticate(self, token_file_path: str=None):
        if not token_file_path:
            raise {'error': 'Not found credential file'}

        with open(token_file_path, 'r') as file:
            data = json.load(file)
            
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        token_uri = data['token_uri']
        client_id = data['client_id']
        client_secret = data['client_secret']
        scopes = data['scopes']
        
        self.creds = Credentials(
            token=access_token,
            refresh_token=refresh_token,
            token_uri=token_uri,
            client_id=client_id,
            client_secret=client_secret,
            scopes=scopes
        )
        
        if not self.creds.valid:
            self.creds.refresh(Request())
            
        return self.creds

    @keyword("Create Course")
    def create_classroom(self, name, ownerId):
        if not self.creds:
            return {'error': 'Authentication failed'}
        
        try:
            service = build("classroom", "v1", credentials=self.creds)
            course = {'name': name, 'ownerId': ownerId}
            created_course = service.courses().create(body=course).execute()

            # Extracting and returning the 'id' field from the created course
            course_id = created_course.get('id')
            return course_id
        except HttpError as error:
            return {'error': str(error)}

    @keyword("List Classrooms")
    def list_classrooms(self):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            courses = service.courses().list().execute()

            if not courses or 'courses' not in courses:
                return {'message': 'No courses found.'}

            courses_list = courses.get('courses', [])
            return [{'name': course['name'], 'id': course['id']} for course in courses_list]
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Delete Classroom")
    def delete_classroom(self, courseId):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)

            # Archieve classroom        
            archive_body = {'courseState': 'ARCHIVED'}
            service.courses().patch(id=courseId, updateMask='courseState', body=archive_body).execute()

            # Then, delete the archived classroom
            service.courses().delete(id=courseId).execute()
            return {'message': f'Classroom with ID {courseId} archived and deleted successfully'}
        except HttpError as error:
            return {'error': str(error)}


    @keyword("Get Course ID By Course Name")
    def get_course_id_by_name(self, course_name):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            results = service.courses().list().execute()
            courses = results.get('courses', [])

            for course in courses:
                if course['name'] == course_name:
                    return course['id']
            return {'error': 'Course not found'}
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Invite Students To Classroom")
    def invite_students_to_classroom(self, courseId, studentEmails):
        if not self.creds:
            return {'error': 'Authentication failed'}
        invited_students = []
        errors = []
        try:
            service = build("classroom", "v1", credentials=self.creds)
            for email in studentEmails:
                try:
                    invitation_body = {
                        'userId': email,
                        'courseId': courseId,
                        'role': 'STUDENT'
                    }
                    invitation = service.invitations().create(body=invitation_body).execute()
                    invited_students.append(invitation)
                except HttpError as error:
                    errors.append(f'Failed to invite {email}: {str(error)}')

            return {'invited_students': invited_students, 'errors': errors}
        except Exception as e:
            return {'error': str(e)}

    @keyword("Create Assignment")
    def create_assignment(self, courseId, title, description, linkMaterials=[], dueDate=None, dueTime=None):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            
            # Prepare link materials
            materials = [{'link': {'url': link}} for link in linkMaterials]

            coursework = {
                'title': title,
                'description': description,
                'materials': materials,  # Add link materials here
                'workType': 'ASSIGNMENT',
                'state': 'PUBLISHED'
            }

            # If due date is provided, add it to the coursework
            if dueDate and dueTime:
                coursework['dueDate'] = dueDate  # dueDate should be a dict like {'year': 2020, 'month': 12, 'day': 15}
                coursework['dueTime'] = dueTime  # dueTime should be a dict like {'hours': 23, 'minutes': 59}
            
            assignment = service.courses().courseWork().create(courseId=courseId, body=coursework).execute()
            return assignment.get('id')
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Create Quiz")
    def create_quiz(self, courseId, title, description, quizUrl, maxPoints, dueDate=None, dueTime=None):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            
            materials = [{
                'link': {
                    'url': quizUrl,
                    'title': title, 
                    'thumbnailUrl': ''
                }
            }]

            coursework = {
                'title': title,
                'description': description,
                'materials': materials,
                'workType': 'ASSIGNMENT',
                'state': 'PUBLISHED',
                'assignment': {
                    'studentWorkFolder': {}
                },
                'maxPoints': maxPoints
            }

            if dueDate and dueTime:
                coursework['dueDate'] = dueDate
                coursework['dueTime'] = dueTime

            quiz = service.courses().courseWork().create(courseId=courseId, body=coursework).execute()
            return quiz.get('id')
        except HttpError as error:
            return {'error': str(error)}

    @keyword("List Coursework")
    def list_coursework(self, courseId):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            response = service.courses().courseWork().list(courseId=courseId).execute()
            coursework_list = response.get('courseWork', [])
            return coursework_list
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Get Coursework ID By Title")
    def get_coursework_id_by_title(self, courseId, title):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            response = service.courses().courseWork().list(courseId=courseId).execute()
            coursework_list = response.get('courseWork', [])

            for coursework in coursework_list:
                if coursework['title'].lower() == title.lower():
                    return coursework['id']

            return 'Coursework with the specified title not found.'
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Get Coursework ID By Title")
    def get_coursework_id_by_title(self, courseId, title):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            response = service.courses().courseWork().list(courseId=courseId).execute()
            coursework_list = response.get('courseWork', [])

            for coursework in coursework_list:
                if coursework['title'].lower() == title.lower():
                    return coursework['id']

            return 'Coursework with the specified title not found.'
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Delete Coursework")
    def delete_coursework(self, courseId, courseworkId):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            service.courses().courseWork().delete(courseId=courseId, id=courseworkId).execute()
            return {'message': f'Coursework with ID {courseworkId} deleted successfully from course {courseId}'}
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("List Student Submissions")
    def list_student_submissions(self, courseId, courseworkId):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            response = service.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId).execute()
            submissions = response.get('studentSubmissions', [])
            return submissions
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Update Student Submission Grade")
    def update_student_submission_grade(self, courseId, courseworkId, submissionId, grade):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)
            submission_body = {
                'assignedGrade': grade,
                'draftGrade': grade
            }
            updated_submission = service.courses().courseWork().studentSubmissions().patch(
                courseId=courseId,
                courseWorkId=courseworkId,
                id=submissionId,
                updateMask='assignedGrade,draftGrade',
                body=submission_body
            ).execute()

            return updated_submission
        except HttpError as error:
            return {'error': str(error)}
        
    @keyword("Get Submission ID By Email")
    def get_submission_id_by_email(self, courseId, courseworkId, studentEmail):
        if not self.creds:
            return {'error': 'Authentication failed'}

        try:
            service = build("classroom", "v1", credentials=self.creds)

            # Fetch all students in the course to find the userId for the given email
            students_response = service.courses().students().list(courseId=courseId).execute()
            students = students_response.get('students', [])
            
            user_id = None
            for student in students:
                if student['profile']['emailAddress'].lower() == studentEmail.lower():
                    user_id = student['userId']
                    break

            if not user_id:
                return 'User ID not found for the provided email'

            # Fetch all submissions and match the userId to find the submissionId
            submissions_response = service.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId).execute()
            submissions = submissions_response.get('studentSubmissions', [])

            for submission in submissions:
                if submission['userId'] == user_id:
                    return submission['id']

            return 'Submission not found for the provided email'
        except HttpError as error:
            return {'error': str(error)}

