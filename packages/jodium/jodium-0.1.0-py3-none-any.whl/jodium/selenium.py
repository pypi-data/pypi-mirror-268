#selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
# webdriver manager modules
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
# utility modules
from random import randrange


if __name__ == '__main__':
    def simple_chrome(page=""):
        options = Options()
        debugging_port = str(randrange(9222, 9999))
        options.add_argument('--remote-debugging-port=%s'%debugging_port)
        service = ChromiumService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        browser.get(page)
        return browser


    browser = simple_chrome("https://github.com")
    browser2 = simple_chrome("https://bing.com")
