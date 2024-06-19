from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer():
    Customers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    Customers_menuitem_xpath="//p[text()=' Customers']"
    Add_button_xpath="//a[@class='btn btn-primary']"
    Email_textfield_id="Email"
    Pass_textfield_id = "Password"
    FirstName_id = "FirstName"
    LastName_id = "LastName"
    Gender_name = "Gender"
    DateOfBirth_id="DateOfBirth"
    Company_name_id="Company"
    Customer_roles_xpath="(//ul[@class='select2-selection__rendered'])[2]"
    #Administration_xpath="//li[@title='Administrators']"
    #Registered_xpath="//li[@title='Registered']"
    Guests_xpath="//li[contains(text(),'Guests')]"
    Manager_Vendor_xpath="//select[@id='VendorId']"
    Admin_content_xpath="//textarea[@id='AdminComment']"
    Save_button_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.Customers_menu_xpath).click()

    def clickOnMenuItem(self):
        self.driver.find_element(By.XPATH, self.Customers_menuitem_xpath).click()

    def addButton(self):
        self.driver.find_element(By.XPATH, self.Add_button_xpath).click()

    def emailTextField(self,email):
        self.driver.find_element(By.ID, self.Email_textfield_id).send_keys(email)

    def passwordTextField(self,passw):
        self.driver.find_element(By.ID, self.Pass_textfield_id).send_keys(passw)

    def firstName(self,fname):
        self.driver.find_element(By.ID, self.FirstName_id).send_keys(fname)

    def lastName(self,lname):
        self.driver.find_element(By.ID, self.LastName_id).send_keys(lname)

    def gender(self):
        self.driver.find_element(By.NAME, self.Gender_name).click()

    def dataOfBirth(self,dob):
        self.driver.find_element(By.ID, self.DateOfBirth_id).send_keys(dob)

    def companyName(self,comname):
        self.driver.find_element(By.ID, self.Company_name_id).send_keys(comname)

    def setCustomerRoles(self):
        self.driver.find_element(By.XPATH,self.Customer_roles_xpath).click()
        time.sleep(3)
        #self.driver.find_element(By.XPATH, "//li//span[text()='×']").click()
        self.driver.find_element(By.XPATH, self.Guests_xpath).click()


    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.Manager_Vendor_xpath))
        time.sleep(2)
        drp.select_by_visible_text(value)

    def adminContent(self,content):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Admin_content_xpath).send_keys(content)

    def clickOnSave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Save_button_xpath).click()