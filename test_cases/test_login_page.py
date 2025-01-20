import os
import time

from selenium.webdriver.common.by import By

from page_objects.Dextris_Login_Page import login_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_001_login:
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
            screenshot_folder = ".\\Screenshots"
            if not os.path.exists(screenshot_folder):
                # Create the folder if it doesn't exist
                os.makedirs(screenshot_folder)

            # Save the screenshot with an absolute path
            screenshot_path = os.path.join(screenshot_folder, "test_title_verification.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            self.driver.close()
            assert False

    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.login_page_url)
        self.login= login_page(self.driver)
        time.sleep(2)
        self.login.set_username_text_field_id(self.username)
        time.sleep(2)
        self.login.set_password_txt_field(self.password)
        time.sleep(2)
        self.login.click_on_login()
        time.sleep(2)
        act_dasboard_txt=self.driver.find_element(By.XPATH,"    //div[text()='Swag Labs']").text
        time.sleep(2)
        if act_dasboard_txt=='Swag Labs':
            assert True
            self.driver.close()
        else:
            # Ensure the Screenshots folder exists
            screenshot_folder = ".\\Screenshots"
            if not os.path.exists(screenshot_folder):
                # Create the folder if it doesn't exist
                os.makedirs(screenshot_folder)

            # Save the screenshot with an absolute path
            screenshot_path = os.path.join(screenshot_folder, "test_valid_login.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            self.driver.close()
            assert False

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
                                                        "text()='Epic sadface: Username and password "
                                                        "do not match any user in this service']").text
        time.sleep(2)
        if error_message=="Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            # Ensure the Screenshots folder exists
            screenshot_folder = ".\\Screenshots"
            if not os.path.exists(screenshot_folder):
                # Create the folder if it doesn't exist
                os.makedirs(screenshot_folder)

            # Save the screenshot with an absolute path
            screenshot_path = os.path.join(screenshot_folder, "test_invalid_login.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            self.driver.close()
            assert False

