import codecs
import os
from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '1.0.5'
DESCRIPTION = 'A tool for predicting the solubility of small molecule drugs.'
LONG_DESCRIPTION = 'There is a specialized tool available for predicting the solubility of small molecule drugs. By analyzing molecular structures and computing various features, it provides accurate predictions crucial for drug discovery. It helps researchers efficiently select and optimize drug candidates. For more information, please refer to our paper.'

# Setting up
setup(
    name="MSCSol",
    version=VERSION,
    author="Ziyu Fan",
    author_email="fzy_csu@qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/ZiyuFanCSU/MSCSol",
    packages=find_packages(),
    include_package_data=True,
)