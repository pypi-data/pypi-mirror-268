"""
@Author: 馒头 (chocolate)
@Email: neihanshenshou@163.com
@File: setup.py
@Time: 2023/12/9 18:00
"""

from setuptools import find_packages
from setuptools import setup

__version__ = "0.1.7.3"

# 包目录下资源
PackageData = ["charset.yaml",
               "common_old.onnx",
               "font/ukai.ttc",
               "browser_session.yaml",
               "config.ini"]

# 依赖的三方库
DependentPackage = [
    "allure-pytest==2.13.2",
    "colorama==0.4.6",
    "func_timeout==4.3.5",
    "NumPy==1.23.5",
    "openpyxl==3.1.0",
    "opencv-python==4.9.0.80",
    "onnxruntime==1.17.1",
    "pandas==2.2.1",
    "Pillow==9.5.0",
    "python-dateutil==2.8.2",
    "pytest==7.3.2",
    "pytest-ordering==0.6",
    "pytest-xdist==3.5.0",
    "PyYAML==6.0",
    "requests==2.30.0",
    "retry==0.9.2",
    "selenium==4.4.3",
    "urllib3==1.26.12",
    "SteamedBread-Uninstall==0.0.4"
]

setup(
    name="SteamedBread",
    author="馒头",
    author_email="neihanshenshou@163.com",
    description="馒头的第三方库",
    long_description=open(file="README.md", encoding="utf-8", mode="r").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    install_requires=DependentPackage,
    license='Apache License 2.0',
    platforms=["MacOS、Window"],
    fullname="馒头大人",
    url="https://github.com/neihanshenshou/SteamedBread"
)
