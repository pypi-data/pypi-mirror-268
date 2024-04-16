"""
@Author: 馒头 (chocolate)
@Email: neihanshenshou@163.com
@File: setup.py
@Time: 2024-03-26 23:19
"""

from setuptools import setup, find_packages

from _CleanPackageTools import CleanDependence

setup(
    name="SteamedBread-Uninstall",
    author="馒头",
    author_email="neihanshenshou@163.com",
    long_description=open(file="README.md", encoding="utf-8", mode="r").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    version=CleanDependence.__version__,
    description="馒头的三方库管理器",
    license='Apache License 2.0',
    platforms=["MacOS、Window"],
    fullname="馒头大人",
    url="https://github.com/neihanshenshou/SteamedBreadPackageManager",
    entry_points=dict(
        console_scripts=[
            "uninstall=_CleanPackageTools.CleanDependence:_start_remove"
        ]
    )
)
