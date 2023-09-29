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


class TestBookingDotCom:

    def test_home_page(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 10)
        driver.get('https://www.booking.com/')
        driver.maximize_window()
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.ID, "accommodations").click()


        # Eta ekta Popup etake popup handler diye handle koro
        popup_close = f"//button[@aria-label='Dismiss sign in information.']"
        driver.find_element(By.XPATH, popup_close).click()
        logging.info(f"popup closed")

        # Select Language
        language= f"//button[@data-testid='header-language-picker-trigger']"
        driver.find_element(By.XPATH, language).click()


        # Select Language as English
        english_language = f"//span[text()='English (UK)']"
        driver.find_element(By.XPATH, english_language).click()
        logging.info(f"English Language selected")

        #select to the destination field and put the destination
        destination_path =f"//div[@data-testid ='destination-container']//input[@placeholder='Where are you going?']"
        destination ='Saint Ann Parish'
        driver.find_element(By.XPATH, destination_path).send_keys(destination)

        # click on the destination field
        # destination_parish =f"//div[@data-testid ='destination-container']//input[@placeholder='Where are you going?'and @value = '{destination}']"
        # driver.find_element(By.XPATH, destination_parish).click()

        #Select Calender
        calender =f"//div[@data-testid='searchbox-dates-container']/.."
        wait.until(EC.element_to_be_clickable((By.XPATH, calender))).click()

        checking_date =f"2023-10-08"
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@data-date = '{checking_date}']"))).click()
        logging.info(f"Checking Date selected as {checking_date}")

        end_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-date = "2023-10-09"]')))
        end_date.click()
        time.sleep(3)
        # driver.quit()