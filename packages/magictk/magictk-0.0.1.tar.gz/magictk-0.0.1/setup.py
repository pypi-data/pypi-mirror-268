import sys
from setuptools import setup, find_packages
VERSION = "0.0.1"
pywin32_need = ([] if sys.platform.startswith("linux") else ["pywin32"])
setup(
    name="magictk",
    version=VERSION,
    packages=(
        find_packages(where="./magictk")
    ),
    package_dir={
        "magictk": "./magictk",
    },
    install_requires=[]+pywin32_need,
    author='cxykevin|git.hmtsai.cn',
    author_email='cxykevin@yeah.net',
    description='A tkinter weights looks like element-plus',
    url='http://git.hmtsai.cn/cxykevin/magictk.git',
    license='GPLv2',
)
