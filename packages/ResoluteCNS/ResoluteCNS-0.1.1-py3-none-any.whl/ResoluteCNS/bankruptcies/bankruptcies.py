from selenium.webdriver.common.by import By

class bankrupcties:
    def __init__(self, driv):
         self._driver = driv
      
    def get(self, courts, from_date, to_date):
            if not self._logged_in:
                self.login()

            #URL of the website     
            url = self._baseurl + "SearchBeta/Bankruptcy"
            self._selfer.get(url)
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
                download_excel = self._driver.find_elements(By.XPATH, "//a[@href='/SearchBeta/GetBankoExcel']/child::img")
                download_excel.click()
            except Exception as e:
                print(e)
            
            return True
    


def validate_court(in_courts, court_to_check):
        result = False
        for c in in_courts:
            if c == court_to_check.text:
                result = True
        return result