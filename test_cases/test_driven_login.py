import os
import time
import pytest
from selenium.webdriver.common.by import By

from screenshots.test_save_scrrenshot import test_save_screenshot
from utilities import XLUtility
from page_objects.Dextris_Login_Page import login_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

path = "C:\\Users\\Lenovo\\PycharmProjects\\nopcommerceApp\\test_data\\data1.xlsx"

class Test_002_datadriven_login:
    login_page_url="https://www.saucedemo.com/"
    username="standard_user"
    password="secret_sauce"
    invalid_user="secret_sauce1"
    #logger=Log_Maker.log_gen()

    # login_page_url=Read_Config.get_login_url()
    # username=Read_Config.get_username()
    # password=Read_Config.get_password()
    # invalid_user=Read_Config.get_invalid_username()

    def test_title_verification(self,setup):
        #self.logger.info("Test case to verify the title of the webpage")
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.login_page_url)
        time.sleep(2)
        act_title=self.driver.title
        exp_title="Swag Labs"
        if act_title==exp_title:
            assert True
            self.driver.close()
        else:
            # Ensure the Screenshots folder exists
            #self.logger.info("If test case failed take the screenshot and store it in Screenshots folder")
            test_save_screenshot(self.driver,"test_title_verification")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.login_page_url)
        self.login= login_page(self.driver)
        time.sleep(2)

        rows=XLUtility.get_cell_count(path,"Sheet1")
        for r in range(2,rows+1):
            username=XLUtility.read_data(path,'Sheet1',r,1)
            password=XLUtility.read_data(path,'Sheet1',r,2)
            self.login.set_username_text_field_id(username)
            time.sleep(2)
            self.login.set_password_txt_field(password)
            time.sleep(2)
            self.login.click_on_login()
            time.sleep(2)
            act_title = self.driver.title
            exp_title = "Swag Labs"
            if act_title == exp_title:
                print("Test is Passed")
                XLUtility.write_data(path, 'Sheet1', r, 3, 'pass')
            else:
                print("Test is Failed")
                XLUtility.write_data(path, 'Sheet1', r, 3, 'file')
                test_save_screenshot(self.driver, "test_valid_login")
        self.driver.close()

    @pytest.mark.smoke
    def test_invalid_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.login_page_url)
        self.login = login_page(self.driver)
        time.sleep(2)
        self.login.set_username_text_field_id(self.invalid_user)
        time.sleep(2)
        self.login.set_password_txt_field(self.password)
        time.sleep(2)
        self.login.click_on_login()
        time.sleep(2)
        error_message=self.driver.find_element(By.XPATH,"//h3[@data-test='error' and "
                                                        "text()='Epic sadface: Userame and password "
                                                        "do not match any user in this servic']").text
        time.sleep(2)
        if error_message=="Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            test_save_screenshot(self.driver, "test_invalid_login")
            self.driver.close()
            assert False

