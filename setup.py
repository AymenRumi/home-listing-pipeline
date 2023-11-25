from setuptools import find_packages, setup

import versioneer


def read_requirements():
    with open("requirements.txt") as req:
        return req.read().splitlines()


setup(
    name="remax_pipeline",
    author="Aymen Rumi",
    author_email='aymen.rumi"mail.mcgill.ca',
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="package to set up data pipeline on aws resources",
    url="https://github.com/AymenRumi/remax-data-pipeline",  # Your project's homepage
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose the appropriate license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
    install_requires=read_requirements(),  # Include the requirements from the requirements.txt file
)
