import email
import time

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.ReadProperties import ReadConfig
import string
import random

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    user_email=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    def test_addCustomer(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.user_email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnMenuItem()
        self.addcust.addButton()

        #self.email=random.random_generator()+"@gmail.com"

        self.addcust.emailTextField("bharath@gmail.com")
        self.addcust.passwordTextField("test123")
        self.addcust.firstName("Bharath")
        self.addcust.lastName("Kumar")
        self.addcust.gender()
        self.addcust.dataOfBirth("8/04/1997")
        self.addcust.companyName("DextQA")
        time.sleep(2)
        self.addcust.setCustomerRoles()
        time.sleep(2)
        self.addcust.setManagerOfVendor("Vendor 2")
        time.sleep(2)
        self.addcust.adminContent("This is for Testing.......")
        time.sleep(2)
        self.addcust.clickOnSave()
        time.sleep(2)



    """def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
     return ''.join(random.choice(chars))"""






