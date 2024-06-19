import time

from utilities.ReadProperties import ReadConfig
from pageObjects.SwagLogin import Login


class Test_001_swaglogin:
    baseUrl=ReadConfig.getUrl()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPasswordfield()

    def test_swaglogin(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)

        self.lgn=Login(self.driver)
        self.lgn.setUserName(self.username)
        time.sleep(2)
        self.lgn.setPassWord(self.password)
        time.sleep(2)
        self.lgn.setLogin()
        time.sleep(2)
        act_title=self.driver.title
        exp_title="Swag Labs"
        if act_title==exp_title:
            print("The title of homepage is correct and it is verified")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_swaglogin.png")
            print("The title of the homepage is not correct and it is verified")
            assert False
        self.driver.quit()
