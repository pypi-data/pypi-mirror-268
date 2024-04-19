import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


if __name__ == '__main__':
    # 指定要测试的APP路径，然后启动APP，并在启动时候指定端口和APP产生的用户数据存放路径
    app_path = r'C:\Users\markh\AppData\Local\Postman\Postman.exe'
    os.system(r'start {} --remote-debugging-port=9222 --user-data-dir="G:\auto"'.format(app_path))
    time.sleep(5)

    # 和操作浏览器区别不大，其中chrome_options已废弃使用会有提示
    # Service中指定chromedriver，这个要与APP内嵌的Chrome版本一致
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "192.168.1.2:9222")
    service = Service(r"D:\Downloads\chromedriver_win32\chromedriver.exe")
    service.start()

    browser = webdriver.Chrome(service=service, options=options)

    time.sleep(2)
    print("先在这个套壳的Chrome上打开百度，然后回退")
    browser.get("https://baidu.com")
    browser.back()
    time.sleep(5)

    wait = WebDriverWait(browser, 5)
    print("browser.title:", browser.title)
    print("browser.current_url:", browser.current_url)
    print("创建新的请求，即将点击 new 按钮")
    new_tab = browser.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]')
    new_tab.click()
