from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Bi-objective Lexicographical Classification'
LONG_DESCRIPTION = ('A package that allows building a matrix with the Bi-objective Lexicographical Classification '
                    'of different algorithms.')

# Setting up
setup(
    name="BiObjClass",
    version=VERSION,
    author="Tiago Costa Soares, Pedro Augusto Mendes, Iago Augusto de Carvalho",
    author_email="tiagocsoares22@gmail.com, pedroaugusto.mendes035@gmail.com, iago.carvalho@unifal-mg.edu.brZ",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['csvkit'],
    keywords=['classification', 'bi-objetive', 'lexicographical', 'ranking', "csv", "bilex", "par10"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)