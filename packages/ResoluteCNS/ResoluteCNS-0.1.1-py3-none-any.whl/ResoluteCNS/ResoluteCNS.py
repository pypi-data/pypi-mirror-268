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

    
    def click_search(self):
        self._driver.find_element(By.ID, 'button_submitbanko').click()
        
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
