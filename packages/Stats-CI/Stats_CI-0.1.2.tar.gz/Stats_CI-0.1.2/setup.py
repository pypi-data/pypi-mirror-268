# from setuptools import setup, find_packages

# setup(
#     name='confidence_interval',
#     version='0.1.0',
#     author='Your Name',
#     author_email='your.email@example.com',
#     packages=find_packages(where="src"),
#     package_dir={"": "src"},
#     url='http://pypi.python.org/pypi/confidence_interval/',
#     license='LICENSE.txt',
#     description='An awesome package for confidence intervals.',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     install_requires=[
#         "numpy",
#         "scipy",
#     ],
# )

import os
from setuptools import setup, find_packages

# Ensure the current directory is correctly set
current_directory = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    with open(os.path.join(current_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    name='Stats_CI',
    version='0.1.2',
    author='Subashanan Nair',
    author_email='your.email@example.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='http://pypi.python.org/pypi/confidence_interval/',
    license='LICENSE.txt',
    description='An awesome package for confidence intervals.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy",
        "scipy",
    ],
)

