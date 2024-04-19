from ._auto_electron import *
from ._install_driver import *
from ._mirror import *
from ._jodium import *
from ._webdriver_manager import *
from undetected_chromedriver import Chrome, ChromeOptions

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
# webdriver manager modules
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


__all__ = ["Chrome", "ChromeOptions", "webdriver", "Options", "ChromiumService", "ChromeDriverManager", "ChromeType"]
__version__ = "0.3.7"


"""
TODO:
- 集成Chrome驱动管理
- 集成隐藏Chrome指纹防反爬
- 根据ip来自动选择最近的ChromeDriver镜像点
- 自动解压下载好的ChromeDriver.zip文件
- 预设驱动下载位置
- 设置环境变量PATH
- 检查ChromeDriver是否成功安装
- 检查ChromeDriver是否于当前Chrome冲突
- 集成并简化对本地Electron APP控制
"""
