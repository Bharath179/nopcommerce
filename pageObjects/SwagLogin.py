from selenium.webdriver.common.by import By


class Login:
    user_name_text_field_id="user-name"
    password_text_field_id="password"
    login_button_id="login-button"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.user_name_text_field_id).send_keys(username)

    def setPassWord(self,password):
        self.driver.find_element(By.ID,self.password_text_field_id).send_keys(password)

    def setLogin(self):
        self.driver.find_element(By.ID,self.login_button_id).click()