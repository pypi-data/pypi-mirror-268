from setuptools import setup, find_packages

VERSION = '0.0.14'
DESCRIPTION = 'Tokenizer Data Values Via NLTK'
LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="tokenizernltk",
    version=VERSION,
    author="PyTorch",
    author_email="<uts@uts.rf.gd>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "transformers",
        "textblob"
    ],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
