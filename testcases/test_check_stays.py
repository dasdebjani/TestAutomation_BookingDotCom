from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class TestBookingDotCom:

    def test_home_page(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # wait = WebDriverWait(driver, 10)
        driver.get('https://www.booking.com/')
        driver.maximize_window()
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.ID, "accommodations").click()
        driver.find_element(By.NAME,"ss").send_keys("Krakow")
        time.sleep(10)
