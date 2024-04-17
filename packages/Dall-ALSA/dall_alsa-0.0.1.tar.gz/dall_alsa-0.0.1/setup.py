from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '0.0.1'
DESCRIPTION = 'This package does Aspect Level Sentiment Analysis on user comments '
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="Dall_ALSA",
        version=VERSION,
        author="Mostafa Amiri",
        author_email="<mostafa.amiri.62@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=['tree-sitter', 'torch','transformers','pandas','googletrans==3.1.0a0','tqdm','re'], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'ALSA', 'dall company'],
        classifiers= [
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
        ]
)