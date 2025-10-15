from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_email_xpath = "//*[contains(@id, 'Email')]"
    textbox_password_xpath = "//*[contains(@id, 'Password')]"
    btn_login_xpath = "//*[text() = 'Log in']"
    logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.logout_linktext).click()














