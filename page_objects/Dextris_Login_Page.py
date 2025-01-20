from selenium.webdriver.common.by import By


class login_page:
    username_text_field_xpath="//input[@id='user-name']"
    password_text_field_id="password"
    login_btn_id="login-button"

    def __init__(self,driver):
        self.driver=driver

    def set_username_text_field_id(self,email):
        self.driver.find_element(By.XPATH,self.username_text_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_text_field_xpath).send_keys(email)

    def set_password_txt_field(self,password):
        self.driver.find_element(By.ID,self.password_text_field_id).clear()
        self.driver.find_element(By.ID, self.password_text_field_id).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.ID, self.login_btn_id).click()
