from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_desc = fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'ICQA / FCMenu automation functions'

# Setting up
setup(
    name="fcmenu",
    version=VERSION,
    author="Adonis N",
    author_email="workamzn@outlook.com",
    description=DESCRIPTION,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['Image', 'pandas', 'selenium'],
    keywords=[],
    classifiers=[
        "Operating System :: Microsoft :: Windows"
    ]
)
