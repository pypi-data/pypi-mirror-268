from setuptools import setup, find_packages


VERSION = '1.0.0'
DESCRIPTION = 'A python libary that gives you access to a set of Ai models including WormGpt , Gemini , blackbox and more'

# Setting up
setup(
    name="LoopAi",
    version=VERSION,
    author="DarkLoop (Organisation)",
    author_email="<private.e.m.a.i.l.0.0.0.1.0.1.0.0.0.1@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'Ai' , 'Text_Models'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)