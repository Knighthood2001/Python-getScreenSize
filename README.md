# Python-getScreenSize

跨平台自动获取屏幕分辨率的 Python 库，支持 Windows 和 Linux 系统。

## 安装

```bash
pip install getScreenSize
```

**说明**：  
- Linux 系统会自动安装依赖 `python3-xlib`，无需手动操作。  
- Windows 系统无额外依赖。

## 使用示例

```python
from getScreenSize import get_screen_size

try:
    width, height = get_screen_size()
    print(f"屏幕分辨率：{width}x{height}")
except Exception as e:
    print(f"获取失败：{e}")
```

## 支持的系统

- Windows（通过 `ctypes` 调用系统 API）
- Linux（通过 `Xlib` 库获取 X11 桌面分辨率，自动安装依赖）



### **核心原理**
1. **条件依赖**：  
   在 `setup.py` 中通过 `sys.platform` 判断系统，仅当为 Linux 时，将 `python3-xlib` 添加到 `install_requires` 列表。  
   这样执行 `pip install getScreenSize` 时：  
   - Linux 环境：pip 会自动下载并安装 `python3-xlib`。  
   - Windows 环境：不安装该依赖，避免冗余。

2. **容错处理**：  
   即使自动安装失败（如网络问题），`core.py` 中仍保留手动安装的提示，确保用户有备选方案。


### **测试验证**
1. **Linux 系统**：  
   执行 `pip install .`（本地安装）或 `pip install screensize`（PyPI 安装），会看到日志中自动安装 `python3-xlib`。

2. **Windows 系统**：  
   安装时不会出现 `python3-xlib` 的相关安装日志，直接可用。
