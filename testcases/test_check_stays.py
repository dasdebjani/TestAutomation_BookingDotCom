from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class TestBookingDotCom:

    def test_home_page(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        feild_path = "//body/div[@id='indexsearch']/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]"
        # wait = WebDriverWait(driver, 10)
        driver.get('https://www.booking.com/')
        driver.maximize_window()
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.ID, "accommodations").click()
        input_field = driver.find_element(By.NAME, "ss")
        input_field.send_keys("Krakow")
        input_field.send_keys(Keys.ENTER)
        time.sleep(10)
