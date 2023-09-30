from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from base.selenium_driver import SeleniumDriver


class StaysPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cookies_path_id = f"onetrust-accept-btn-handler"
    stay_page_id = f"accommodations"
    # tittle_path = f"//span[@data-testid='herobanner-title1']"
    popup_close_path = f"//button[@aria-label='Dismiss sign in information.']"
    language_path = f"//button[@data-testid='header-language-picker-trigger']"
    english_language_path = f"//span[text()='English (UK)']"
    destination_path = f"//div[@data-testid ='destination-container']//input[@placeholder='Where are you going?']"

    calender_path = f"//div[@data-testid='searchbox-dates-container']/.."
    checking_date_path = f"//span[@data-date = '2023-10-08']"

    checkout_date_path = f"//span[@data-date = '2023-10-09']"
    occupancy_path = f"//button[@data-testid='occupancy-config']"

    adult_element_path = f"//div[@data-testid='occupancy-popup']/div/div/div/following::div/button[1]"
    search_button_path = f"//span[contains(text(), 'Search') and @class = 'e4adce92df']"

    # All actions
    def clickStaysButton(self):
        self.elementClick(self.stay_page_id, locatorType="id")

    def clickAcceptCookies(self):
        self.elementClick(self.cookies_path_id, locatorType="id")

    def clickPopup(self):
        self.elementClick(self.popup_close_path, locatorType="xpath")

    def clickLanguage(self):
        self.elementClick(self.language_path, locatorType="xpath")

    def clickLanguageEnglish(self):
        self.elementClick(self.english_language_path, locatorType="xpath")

    def clickDestination(self, destinationName):
        self.sendKeys(destinationName, self.destination_path, locatorType="xpath")

    def clickCalender(self):
        self.elementClick(self.calender_path, locatorType="xpath")

    def clickCheckingDate(self):
        self.elementClick(self.checking_date_path, locatorType="xpath")

    def clickCheckOutDate(self):
        self.elementClick(self.checkout_date_path, locatorType="xpath")

    def clickOccupancy(self):
        self.elementClick(self.occupancy_path, locatorType="xpath")

    def clickAdultSelect(self):
        self.elementClick(self.adult_element_path, locatorType="xpath")

    def clickSearchButton(self):
        self.elementClick(self.search_button_path, locatorType="xpath")

    def stays(self, destination):
        self.clickAcceptCookies()
        self.clickStaysButton()
        self.clickPopup()
        self.clickPopup()
        self.clickLanguage()
        self.clickLanguageEnglish()
        self.clickDestination(destination)
        self.clickCalender()
        self.clickCheckingDate()
        self.clickCheckOutDate()
        self.clickCheckOutDate()
        self.clickOccupancy()
        self.clickAdultSelect()
        self.clickSearchButton()
