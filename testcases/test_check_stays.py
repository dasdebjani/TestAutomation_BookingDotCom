from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import logging
from pages.stays.stays_page import StaysPage
import unittest


class TestBookingDotCom(unittest.TestCase):

    def test_home_page(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        base_url = "https://www.booking.com/"
        driver.maximize_window()
        driver.get(base_url)
        object_stays_page = StaysPage(driver)
        object_stays_page.stays("Saint Ann Parish")


        #Scroll down
        # driver.execute_script("window.scrollBy(0,674);")

        time.sleep(5)
        driver.quit()