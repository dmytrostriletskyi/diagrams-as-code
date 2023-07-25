"""
Setup the package.
"""
from setuptools import (
    find_packages,
    setup,
)

with open('README.md', 'r', encoding='utf-8') as read_me:
    long_description = read_me.read()

with open('requirements/project.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('.project-version', 'r') as project_version_file:
    project_version = project_version_file.read().strip()

setup(
    version=project_version,
    name='diagrams-as-code',
    description='Diagrams as code: declarative configurations using YAML for drawing cloud system architectures.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dmytrostriletskyi/diagrams-as-code',
    project_urls={
        'Issue Tracker': 'https://github.com/dmytrostriletskyi/diagrams-as-code/issues',
        'Source Code': 'https://github.com/dmytrostriletskyi/diagrams-as-code',
        'Download': 'https://github.com/dmytrostriletskyi/diagrams-as-code/tags',
    },
    license='MIT',
    author='Dmytro Striletskyi',
    author_email='dmytro.striletskyi@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    entry_points={
        'console_scripts': [
            'diagrams-as-code = diagrams_as_code.entrypoint:entrypoint',
        ],
    },
)
