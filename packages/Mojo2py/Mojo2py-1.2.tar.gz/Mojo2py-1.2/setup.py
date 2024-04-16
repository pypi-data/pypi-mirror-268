from setuptools import setup, find_packages
import pkg_resources

VERSION = '1.2'
DESCRIPTION = 'A python package which converts a mojo file (.mojo or .🔥) into a python file.'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Mojo2py",
    version="1.2",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vishal",
    author_email="vishalvenkat2604@gmail.com",
    license='MIT',
    packages=find_packages(),
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
    url="https://github.com/venvis/mojo2py",
    package_data={'mojo2py': ['mojo.json']},
   
)
with pkg_resources.resource_stream("mojo2py", 'mojo.json') as f:
  mojo_data = f.read()