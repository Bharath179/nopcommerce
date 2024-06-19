import time

from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities import XLUtitity


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/Data1.xlsx"


    def test_login_ddt(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.login=LoginPage(self.driver)

        self.rows=XLUtitity.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel is:",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtitity.readData(self.path,'Sheet1',r,1)
            self.password = XLUtitity.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtitity.readData(self.path, 'Sheet1', r, 3)

            self.login.setUserName(self.user)
            self.login.setPassword(self.password)
            self.login.clickLogin()
            time.sleep(2)

            act_title=self.driver.title
            #print("Title of the HomePage is:",title)
            exp_title="Dashboard / nopCommerce administration"

        if act_title==exp_title:
              if self.exp=='Pass':

               self.login.clickLogout()

               lst_status.append("Passed")
              elif self.exp=="Fail":

               self.login.clickLogout()

               lst_status.append("Fail")
        elif act_title !=exp_title:
            lst_status.append("Pass")
            if self.exp == 'Pass':
             lst_status.append("Fail")
            elif self.exp=='Fail':
             lst_status.append("Pass")

        if "Fail" not in lst_status:
                print("Login DDT test passed.....")
                self.driver.close()
                assert True
        else:
                print("Login DDT test failed.....")
                self.driver.close()
                assert False
