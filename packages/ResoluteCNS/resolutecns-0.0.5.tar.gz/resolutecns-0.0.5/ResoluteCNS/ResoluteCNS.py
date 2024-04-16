#importing webdriver from selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import FirefoxOptions
import time
import pandas as pd
import platform
from os.path import expanduser
import os
import urllib
from datetime import datetime

username = 'jdingman@resolutecommercial.com'
password = 'ResComm!1'


class CNS:

    def __init__(self, opts):
        self._logged_in = False
        self._username = username
        self._password = password
        self._opts = opts
        self._driver = webdriver.Firefox(options=opts)
        self._driver.install_addon('uBlock0.xpi', temporary=True)
        self._baseurl = "https://cnsplus.courthousenews.com/"

    def login(self):
        print('Logging in')
        username_field = self._driver.find_element(By.ID, 'UserName')
        username_field.send_keys(username)
        time.sleep(2)
        password_field = self._driver.find_element(By.ID, 'Password')
        password_field.send_keys(password)
        time.sleep(2)
        login_button = self._driver.find_element(By.CLASS_NAME, 'submitbutton')
        login_button.click()
        #time.sleep(10)
        self._logged_in = True
        print('Logged in')

    def get_bankruptcies(self, courts, from_date, to_date):
        #URL of the website     
        url = self._baseurl + "SearchBeta/Bankruptcy"
        self._driver.get(url)
        self.setup_filters(courts, from_date, to_date)
        self.click_search()
        return self.download_excel()
        
    def setup_filters(self, in_courts, from_date, to_date):

        from_date_field = self._driver.find_element(By.CLASS_NAME, 'datepicker')
        from_date_field.send_keys(from_date)

        #driver.find_elements(By.NAME, 'BankoCourts')
        courts = self._driver.find_elements(By.XPATH, "//input[@name='BankoCourts']/following-sibling::label")

        for court in courts:
            if self.validate_court(in_courts, court):
                court_check = self._driver.find_element(By.ID, court.get_attribute('for'))
                court_check.click()


    def validate_court(in_courts, court_to_check):
        result = False
        for c in in_courts:
            if c == court_to_check.text:
                result = True
        return result


    def click_search(self):
        self._driver.find_element(By.ID, 'button_submitbanko').click()

    def download_excel(self):
        self._driver.set_page_load_timeout(10)
        try:
            self._driver.get('https://cnsplus.courthousenews.com/SearchBeta/GetBankoExcel')
        except Exception as e:
            print(e)
        
        #Open the file
        df = pd.read_excel(download_folder('SearchResults.xlsx'))
        return df

    
def download_folder(filename):
    home = os.path.expanduser("~")
    download_path = home + os.sep + "Downloads"
    if platform.system() == "Darwin" or "Linux":
        return download_path + "/" + filename
    else:
        return download_path + "\\" + filename



