from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


class StaysPage():

    def __init__(self, driver):
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
    occupancy_path = f"//button[@data-testid='occupancy-config']"
    calender_path = f"//div[@data-testid='searchbox-dates-container']/.."
    checking_date_path = f"//span[@data-date = '2023-10-08']"
    checkout_date_path = f"//span[@data-date = '2023-10-09']"
    occupancy_path = f"//button[@data-testid='occupancy-config']"
    adult_element_path = f"//div[@data-testid='occupancy-popup']/div/div/div/following::div/button[1]"
    search_button_path = f"//span[contains(text(), 'Search') and @class = 'e4adce92df']"


   # Get Element Method
    def getCookieElement(self):
        return self.driver.find_element(By.ID, self.cookies_path_id)

    def getStayPageElement(self):
        return self.driver.find_element(By.ID, self.stay_page_id)

    # def getTittle(self):
    #     return self.driver.find_element(By.XPATH, self.tittle_path)

    def getPopupElement(self):
        return self.driver.find_element(By.XPATH, self.popup_close_path)

    def getLanguageElement(self):
        return self.driver.find_element(By.XPATH, self.language_path)

    def getSelectLanguageElement(self):
        return self.driver.find_element(By.XPATH, self.english_language_path)

    def getDestinationElement(self):
        return self.driver.find_element(By.XPATH, self.destination_path)

    def getCalenderElement(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.calender_path)))

    def getCheckingDateElement(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.checking_date_path)))

    def getCheckOutElement(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_date_path)))

    def getOccupancyElement(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.occupancy_path)))

    def getAdultsSelectElement(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.adult_element_path)))

    def getSearchButtonElement(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button_path)))



    #Actions Method
    def clickAcceptCookies(self):
        self.getCookieElement().click()

    def clickStaysButton(self):
        self.getStayPageElement().click()

    def clickPopup(self):
        self.getPopupElement().click()

    def clickLanguage(self):
        self.getLanguageElement().click()

    def clickLanguageEnglish(self):
        self.getSelectLanguageElement().click()

    def clickDestination(self,destinationName):
        self.getDestinationElement().send_keys(destinationName)

    def clickCalender(self):
        self.getCalenderElement().click()

    def clickCheckingDate(self):
        self.getCheckingDateElement().click()

    def clickCheckOutDate(self):
        self.getCheckOutElement().click()

    def clickOccupancy(self):
        self.getOccupancyElement().click()

    def clickAdultSelect(self):
        self.getAdultsSelectElement().click()

    def clickSearchButton(self):
        self.getSearchButtonElement().click()


    def stays(self,destination):

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