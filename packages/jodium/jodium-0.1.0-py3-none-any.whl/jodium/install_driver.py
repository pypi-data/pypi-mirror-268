import platform
import re
import subprocess

import requests
import zipfile
from io import BytesIO
import os


if __name__ == '__main__':
    # 获取 Chrome 浏览器版本号
    from selenium.webdriver.chrome.service import Service

    command_output = subprocess.run(
        ['wmic', 'datafile', 'where', 'name="C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe"',
        'get', 'Version', '/value'], capture_output=True)
    version_string = command_output.stdout.decode().strip()

    chrome_version = re.search(r'(\d+\.\d+\.\d+\.\d+)', version_string).group(1)

    print(f'The current version of Chrome is {chrome_version}')

    # 下载最新版本的 ChromeDriver
    response = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
    latest_version = response.text.strip()

    download_url = f'https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_win32.zip'
    response = requests.get(download_url)

    if response.status_code == 200:
        try:
            with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
                zip_file.extractall(os.getcwd())
            print('ChromeDriver has been updated!')
        except zipfile.BadZipFile:
            print('The downloaded file is not a valid ZIP file!')

        # 指定 ChromeDriver 可执行文件的路径
        system_bit = platform.architecture()[0]
        print(system_bit)
        # executable_path = os.path.join(os.getcwd(), f'chromedriver_{system_bit}.exe')
        executable_path = os.path.join(os.getcwd(), f'chromedriver.exe')
        print(executable_path)

        # ChromeDriver所在文件夹的完整路径
        # chromedriver_path = r"C:\chromedriver_win32"
        chromedriver_path = executable_path
        # 获取当前系统的PATH环境变量
        path_env = os.environ['PATH']
        # print(path_env)
        # 将ChromeDriver路径添加到PATH环境变量中，并用分号分隔
        os.environ['PATH'] = path_env + ";" + chromedriver_path

        path_env = os.environ['PATH']
        print(path_env)
        # print(type(path_env))
        # s = path_env.split(";")
        # print(type(s))
        # for i in s:
        #     print(i)

        # 检查 ChromeDriver 是否与本地 Chrome 浏览器版本兼容
        from selenium import webdriver

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        service = Service(executable_path=executable_path)
        driver = webdriver.Chrome(service=service, options=options)

        local_version = driver.capabilities['browserVersion']
        if chrome_version.split('.')[0] == local_version.split('.')[0]:
            print(f'The downloaded ChromeDriver version {latest_version} is compatible with your Chrome browser version.')
        else:
            print(
                f'The downloaded ChromeDriver version {latest_version} may not be compatible with your Chrome browser version. Local version: {local_version}')

        driver.quit()

    else:
        print(f'Failed to download ChromeDriver. Status code: {response.status_code}')

