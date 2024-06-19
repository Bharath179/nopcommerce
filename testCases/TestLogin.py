import time

from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    def test_login(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.login=LoginPage(self.driver)
        time.sleep(2)
        self.login.setUserName(self.username)
        time.sleep(2)
        self.login.setPassword(self.password)
        time.sleep(2)
        self.login.clickLogin()
        time.sleep(2)
        title=self.driver.title
        print("Title of the HomePage is:",title)
        exp_title="Dashboard / nopCommerce administration"
        if title==exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.login.clickLogout()
            self.driver.close()

            assert False











