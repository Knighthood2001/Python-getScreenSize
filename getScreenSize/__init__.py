"""
screensize: 跨平台获取屏幕分辨率的 Python 库
支持 Windows 和 Linux 系统
"""

__version__ = "0.1.0"  # 库的版本号

from .core import get_screen_size  # 暴露核心函数，用户可直接导入
