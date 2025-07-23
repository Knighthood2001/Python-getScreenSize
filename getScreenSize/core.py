import sys

def get_screen_size_windows():
    """获取 Windows 系统屏幕分辨率（宽 x 高）"""
    try:
        import ctypes
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    except Exception as e:
        raise RuntimeError(f"Windows 分辨率获取失败: {e}") from e

def get_screen_size_linux():
    """获取 Linux 系统屏幕分辨率（宽 x 高）"""
    try:
        from Xlib.display import Display
        display = Display()
        screen = display.screen()
        return screen.width_in_pixels, screen.height_in_pixels
    except ImportError as e:
        raise ImportError(
            "Linux 环境需要 Xlib 库，请先安装：\n"
            "pip install python3-xlib"
        ) from e
    except Exception as e:
        raise RuntimeError(f"Linux 分辨率获取失败: {e}") from e

def get_screen_size():
    """
    获取当前系统的屏幕分辨率（跨平台支持）
    
    返回值：
        tuple: (宽度, 高度)，单位为像素
        None: 不支持的系统或获取失败
    """
    if sys.platform.startswith('win'):
        return get_screen_size_windows()
    elif sys.platform.startswith('linux'):
        return get_screen_size_linux()
    else:
        raise OSError(f"不支持的操作系统: {sys.platform}")
