from setuptools import setup, find_packages

# Read the contents of README.md
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='sharepoint_utils',
    version='0.2',
    author='Omkar Sutar',
    description='Utility functions for working with SharePoint files',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This tells setuptools that the long description is in Markdown format
    packages=find_packages(),
    install_requires=[
        'pandas',
        'Office365-REST-Python-Client'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
