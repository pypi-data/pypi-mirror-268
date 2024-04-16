from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="The Crypt Master",
    version='0.0.31',
    author="Huth S0lo",
    author_email="john@themorphium.io",
    description="Crypt Master Client for use with a Crypt Master Server",
    url = "https://github.com/TheCryptMaster/CryptMaster",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pycryptodome', 'httpx', 'argon2-cffi', 'platformdirs', 'pypedreams'],
    keywords=['pypi', 'cicd', 'python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)