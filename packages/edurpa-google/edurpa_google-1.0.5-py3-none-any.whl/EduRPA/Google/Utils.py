from robot.api.deco import keyword
from CustomOAuth import CustomOAuth

class Utils:
    def __init__(self):
        self.oauth = CustomOAuth()

    @keyword("Set up OAuth token in vault")
    def set_up_oauth_token_file(self, token_file_path):
        self.oauth.set_up_oauth_token_file(token_file_path)