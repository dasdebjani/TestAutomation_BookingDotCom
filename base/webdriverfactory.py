import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory():

    def __init__(self,browser):
        self.browser = browser

    def getWebdriverInstance(self):

        baseURL = "https://www.booking.com/"
        if self.browser == 'chrome':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif self.browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.maximize_window()
        driver.get(baseURL)
        time.sleep(3)

        return driver



