from selenium.webdriver.common.by import By
from ResoluteCNS import ResoluteCNS

class Bankruptcies:
    def __init__(self):
      pass

    def get(self, courts, from_date, to_date):
            if not cns._logged_in:
                cns.login()

            #URL of the website     
            url = self._baseurl + "SearchBeta/Bankruptcy"
            cns._driver.get(url)
            self.setup_date_filters(from_date, to_date)
            self.setup_court_filters(courts)
            self.click_search()
            return self.download_excel()

    def setup_date_filters(self, from_date, to_date):
        from_date_field = ResoluteCNS.CNS._driver.find_element(By.CLASS_NAME, 'datepicker')
        from_date_field.send_keys(from_date)
        
    def setup_court_filters(self, in_courts):

        courts = ResoluteCNS.CNS._driver.find_elements(By.XPATH, "//input[@name='BankoCourts']/following-sibling::label")

        for court in courts:
            if validate_court(in_courts, court):
                court_check = ResoluteCNS.CNS._driver.find_element(By.ID, court.get_attribute('for'))
                court_check.click()


    def click_search(self):
        ResoluteCNS.CNS._driver.find_element(By.ID, 'button_submitbanko').click()
        

    def download_excel(self):
            ResoluteCNS.CNS._driver.set_page_load_timeout(10)
            try:
                download_excel = ResoluteCNS.CNS._driver.find_elements(By.XPATH, "//a[@href='/SearchBeta/GetBankoExcel']/child::img")
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