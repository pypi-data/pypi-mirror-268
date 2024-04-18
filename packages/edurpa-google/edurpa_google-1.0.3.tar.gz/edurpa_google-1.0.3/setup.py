import pathlib
import setuptools
import pkg_resources

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with pathlib.Path('./requirements.txt').open() as requirements_txt:
    requirements = requirements_txt.readlines()
    install_requires = [
            str(requirement)
            for requirement
            in pkg_resources.parse_requirements(requirements)
        ]

setuptools.setup(
    name="edurpa_google",
    version="1.0.3",
    author="david",
    author_email="davidhuynh0222@gmail.com",
    description="Education Google RPA Librabry For Education",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edu-rpa/edu-rpa-library",
    package_dir={'': 'src/EduRPA/'},
    packages=setuptools.find_packages(where='src/EduRPA/Google'),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = install_requires,
)
