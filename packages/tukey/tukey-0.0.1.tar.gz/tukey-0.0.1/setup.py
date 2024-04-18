from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A basic python based maths package'

# Setting up
setup(
    name="tukey",
    version=VERSION,
    author="NeuronZero (Shubhranil Basak)",
    author_email="<Shubhranil.Basak@iiitb.ac.in>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)