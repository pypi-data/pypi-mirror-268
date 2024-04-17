# this file contains some placeholders
# that are changed in a local copy if a release is made

import setuptools

README = 'README.md'  # the path to your readme file
README_MIME = 'text/markdown'  # it's mime type

with open(README, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kato",
    version="1.0.0",
    author="ameasere",
    author_email="leigh@ameasere.com",
    description="NetCloud24 Cryptographic POC",
    url="https://github.com/ameasere/kato",
    long_description=long_description,
    long_description_content_type=README_MIME,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ],
    install_requires=["aeskeyschedule"
    ]
)
