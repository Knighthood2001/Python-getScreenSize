import sys
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# 条件依赖：Linux 系统需要 python3-xlib，Windows 不需要
install_requires = []
if sys.platform.startswith('linux'):
    install_requires.append('python3-xlib')  # Linux 自动安装 xlib

setup(
    name="getScreenSize",
    version="0.1.1",  # 版本号更新
    author="knighthood",
    author_email="your@email.com",
    description="跨平台自动获取屏幕分辨率（Linux 自动安装依赖）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Knighthood2001/Python-getScreenSize",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,  # 动态依赖列表
)
