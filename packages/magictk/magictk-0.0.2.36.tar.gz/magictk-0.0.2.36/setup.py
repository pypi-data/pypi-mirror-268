import sys
import os
from setuptools import setup, find_packages

####### config #######
VERSION = "0.0.2"
######################

set_v = VERSION
if (os.path.exists("runid.conf")):
    with open("runid.conf", "r") as file:
        runid = file.read()
    set_v = set_v+"."+runid
else:
    set_v = set_v+"."+"1000"

print("BUILD: version="+set_v)

setup(
    name="magictk",
    version=set_v,
    packages=find_packages(),
    package_dir={
        "magictk": "./magictk",
    },
    install_requires=[],
    author='cxykevin|git.hmtsai.cn',
    author_email='cxykevin@yeah.net',
    description='A tkinter weights looks like element-plus',
    url='http://git.hmtsai.cn/cxykevin/magictk.git',
    license='GPLv2',
)
