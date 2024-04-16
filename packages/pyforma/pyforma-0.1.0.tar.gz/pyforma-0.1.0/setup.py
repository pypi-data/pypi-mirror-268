import pathlib
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent

# Package metadata
NAME = 'pyforma'
VERSION = '0.1.0'
DESCRIPTION = 'Create and Version HTML forms directly from a Dataclass'
AUTHOR = 'Jayden Rasband'
AUTHOR_EMAIL = 'jayden.rasband@gmail.com'
URL = 'https://github.com/jrasband-dev/pyforma'
LICENSE = 'MIT'

# Long description from README.md file
README = (HERE / "README.md").read_text()

# Requirements
REQUIREMENTS = [
    'jinja2',

]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=['pyforma'],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # Add more classifiers as needed
    ],
    python_requires='>=3.7',  # Specify minimum Python version
)
