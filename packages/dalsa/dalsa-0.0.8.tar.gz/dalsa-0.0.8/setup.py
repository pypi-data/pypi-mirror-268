# from setuptools import setup, find_packages
# from pathlib import Path
# this_directory = Path(__file__).parent

# VERSION = '0.0.4'
# DESCRIPTION = 'This package does Aspect Level Sentiment Analysis(ALSA) on user comments about a given product'
# LONG_DESCRIPTION = (this_directory / "README.md").read_text()




# # Setting up
# setup(
#        # the name must match the folder name 'verysimplemodule'
#         name="alsa",
#         version=VERSION,
#         author="Mostafa Amiri",
#         author_email="<mostafa.amiri.62@gmail.com>",
#         description=DESCRIPTION,
#         long_description=LONG_DESCRIPTION,
#         long_description_content_type='text/markdown',
#         packages=find_packages(),
#         install_requires=['regex', 'torch','transformers','pandas','googletrans==3.1.0a0','tqdm','regex'], # add any additional packages that
#         # needs to be installed along with your package. Eg: 'caer'

#         keywords=['python', 'crawler', 'dall company'],
#         classifiers= [
#                 "Programming Language :: Python :: 3",
#                 "License :: OSI Approved :: MIT License",
#                 "Operating System :: OS Independent",
#         ]
# )
import subprocess
from setuptools import setup, find_packages
from pathlib import Path



# Get the current directory
this_directory = Path(__file__).parent

# Read README.md for long description
LONG_DESCRIPTION = (this_directory / "README.md").read_text()



# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="dalsa",
    version='0.0.8',
    author="Mostafa Amiri",
    author_email="<mostafa.amiri.62@gmail.com>",
    description="This package does Aspect Level Sentiment Analysis (ALSA) on user comments about a given product",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['regex', 'torch', 'transformers', 'pandas', 'googletrans==3.1.0a0', 'tqdm', 'regex'], # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=['python', 'crawler', 'dall company'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
