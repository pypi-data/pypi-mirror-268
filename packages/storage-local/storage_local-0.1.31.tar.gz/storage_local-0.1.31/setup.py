import setuptools
 
setuptools.setup(
    name='storage-local',
    version='0.1.31',  # https://pypi.org/project/storage-local/
    author="Circles",
    author_email="info@circle.zone",
    description="PyPI Package for Circles Storage functions",
    long_description="This is a package for sharing common S3 function used in different repositories",
    long_description_content_type="text/markdown",
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
    ],
    install_requires=["boto3>=1.28.44",
                    "logger-local>=0.0.41",
                    "user-context-remote>=0.0.18"]
)
