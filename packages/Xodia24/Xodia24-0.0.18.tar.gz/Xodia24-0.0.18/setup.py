from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()



VERSION = '0.0.18' 
DESCRIPTION = 'Python package providing a custom environment for simulating tank battles'
LONG_DESCRIPTION = 'Xodia24 is a Python package providing a custom environment for simulating a tank battle scenario where two tanks are positioned on a 2D grid.'

# Setting up
setup(
    name="Xodia24",
    version=VERSION,
    author="Prem Gaikwad",
    author_email="premgaikwad7a@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['gymnasium', 'numpy', 'matplotlib'],
    keywords=['python', 'reinforcement-learning', 'tank-battle'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
