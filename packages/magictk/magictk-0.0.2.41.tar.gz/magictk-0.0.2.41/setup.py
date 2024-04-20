import sys
import os
from setuptools import setup

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

print("----- setup -----")
setup(
    name="magictk",
    version=set_v,
    packages=("magictk",),
    package_dir={
        "magictk": "./magictk",
    },
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=[],
    author='cxykevin|git.hmtsai.cn',
    author_email='cxykevin@yeah.net',
    description='A tkinter weights looks like element-plus',
    long_description='',
    url='http://git.hmtsai.cn/cxykevin/magictk.git',
    license='GPLv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
