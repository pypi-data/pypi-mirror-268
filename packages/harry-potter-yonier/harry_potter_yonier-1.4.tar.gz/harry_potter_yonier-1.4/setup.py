from pathlib import Path # > 3.6
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = 'v1.4'
DESCRIPTION = 'Permite consumir el API de Harry Potter para obtener o listar personajes'
PACKAGE_NAME = 'harry_potter_yonier'
AUTHOR = 'Yonier Asprilla'
EMAIL = 'yoonier13@gmail.com'
GITHUB_URL = 'https://github.com/YonierGomez/harrypotter_python'

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points={
        "console_scripts":
            ["yonierpotter=harry_potter_yonier.__main__:call_me"]
    },
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'harrypotter'
    ],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)