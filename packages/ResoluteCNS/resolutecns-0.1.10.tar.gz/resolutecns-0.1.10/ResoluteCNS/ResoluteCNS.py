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
from pkg_resources import resource_filename

username = 'jdingman@resolutecommercial.com'
password = 'ResComm!1'


class CNS:

    def __init__(self):
        self._logged_in = False
        self._username = username
        self._password = password
        self._opts = FirefoxOptions()
        self._ublock_path = resource_filename('ResoluteCNS', 'uBlock0.xpi')
        self._driver = None
        

    def login(self):
        self._driver = webdriver.Firefox(options=self._opts)
        self._driver.install_addon(self._ublock_path, temporary=True)
        self._baseurl = "https://cnsplus.courthousenews.com/"
        self._driver.get(self._baseurl)
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
        return self._logged_in

    def get_bankruptcies(self, courts, from_date, to_date):
        if not self._logged_in:
            self.login()

        #URL of the website     
        url = self._baseurl + "SearchBeta/Bankruptcy"
        self._driver.get(url)
        self.setup_date_filters(from_date, to_date)
        self.setup_court_filters(courts)
        self.click_search()
        return self.download_excel()
    
    def setup_date_filters(self, from_date, to_date):
        from_date_field = self._driver.find_element(By.CLASS_NAME, 'datepicker')
        from_date_field.send_keys(from_date)
        
        
    def setup_court_filters(self, in_courts):

        courts = self._driver.find_elements(By.XPATH, "//input[@name='BankoCourts']/following-sibling::label")

        for court in courts:
            if validate_court(in_courts, court):
                court_check = self._driver.find_element(By.ID, court.get_attribute('for'))
                court_check.click()


    def click_search(self):
        self._driver.find_element(By.ID, 'button_submitbanko').click()

    def download_excel(self):
        self._driver.set_page_load_timeout(10)
        try:
            download_excel = self._driver.find_element(By.XPATH, "//a[@href='/SearchBeta/GetBankoExcel']/child::img")
            download_excel.click()
        except Exception as e:
            print(e)
        
        #Open the file
        df = pd.read_excel(download_folder('SearchResults.xlsx'))
        return df

    def get_complaints(self, states=None, counties=None, from_date=None, to_date=None):
        if not self._logged_in:
            self.login()

        now = datetime.now()
        
        if not from_date:
            from_date = now.strftime("%m/%d/%Y")
        if not to_date:
            from_date = now.strftime("%m/%d/%Y")

        #URL of the website     
        url = self._baseurl + "SearchBeta/Complaints"
        self._driver.get(url)
        time.sleep(1)
        self.setup_date_filters(from_date, to_date)

        if states:
            self.set_state_filters(states)
        if counties:
            self.set_county_filters(counties)
        
        self.click_search_complaints()
        time.sleep(5)

        return self.download_excel_complaints()


    def download_excel_complaints(self):
        self._driver.set_page_load_timeout(10)
        try:
            download_excel = self._driver.find_element(By.XPATH, "//a[@href='/SearchBeta/GetComplaintsExcel']/child::img")
            download_excel.click()
        except Exception as e:
            print(e)
        
        #Open the file
        df = pd.read_excel(download_folder('SearchResults.xlsx'))
        return df

    def set_state_filters(self, in_states):
        states = self._driver.find_elements(By.XPATH, "//input[@name='States']")

        for state in states:
            if validate_state(in_states, state):
                state.click()
    
    def set_county_filters(self, in_counties):
        states = self._driver.find_elements(By.XPATH, "//input[@name='States']")
        in_states = list(in_counties.keys())

        for state in states:
            if validate_state(in_states, state):
                state_name = state.get_attribute('id')
                self._driver.find_element(By.XPATH, f"//div[contains(text(), '{state_name}')][@class='statealphabutton']").click()
                time.sleep(2)
                
                for county in in_counties[state_name]:
                    self._driver.find_element(By.XPATH, f"//label[contains(text(), '{county}')]").click()
                
                self._driver.find_element(By.XPATH, f"//span[@onclick='ShowStates();']").click()
                time.sleep(2)
        
    
    def click_search_complaints(self):
        self._driver.find_element(By.ID, 'button_submittop').click()

def download_folder(filename):
    home = os.path.expanduser("~")
    download_path = home + os.sep + "Downloads"
    if platform.system() == "Darwin" or "Linux":
        return download_path + "/" + filename
    else:
        return download_path + "\\" + filename

def validate_state(in_states, state_to_check):
    result = False
    for s in in_states:
        if s == state_to_check.get_attribute('id'):
            result = True
    return result

def validate_court(in_courts, court_to_check):
        result = False
        for c in in_courts:
            if c == court_to_check.text:
                result = True
        return result