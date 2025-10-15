import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer_Page:

    # locators from Add customer page
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    link_customer_menuoption_xpath = "//a[@href='/Admin/Customer/List']//p"
    link_addnew_xpath = "//a[@href='/Admin/Customer/Create']//i"
    customer_info_xpath = "//*[contains(text(), 'Customer info')]"
    text_email_xpath = "//*[@id='Email']"
    text_password_xpath = "//*[@id='Password']"
    text_firstname_xpath = "//*[@id='FirstName']"
    text_lastname_xpath = "//*[@id='LastName']"
    rdbtn_male_xpath = "//*[@id='Gender_Male']"
    rdbtn_female_xpath = "//*[@id='Gender_Female']"
    label_cname_xpath = "//*[@id='Company']"
    taxexempt_xpath = "//*[@id = 'IsTaxExempt']"
    newsletter_xpath = "//div[@class='input-group-append']//input[@role='searchbox']"
    select_newspaper_xpath = "//li[contains(text(), 'nopCommerce admin demo store')]"
    cusrole_xpath = "//div[@class='input-group-append input-group-required']//ul[@class='select2-selection__rendered']"
    cusrole_registered_xpath = "//ul[@id='select2-SelectedCustomerRoleIds-results']//li[contains(text(), 'Registered')]"
    cusrole_guests_xpath = "//li[contains(text(), 'Guests')]"
    cusrole_administrators_xpath = "//li[contains(text() = 'Administrators')]"
    cusrole_forummoderators_xpath = "//li[contains(text() = 'Forum Moderators')]"
    cusrole_vendors_xpath = "//li[contains(text() = 'Vendors')]"
    managerofvndor_id = "VendorId"
    text_admincomment_id = "AdminComment"
    save_button_xpath = "//button[@name = 'save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customers(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()

    def click_customers_in_menu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menuoption_xpath).click()

    def click_addNew(self):
        self.driver.find_element(By.XPATH, self.link_addnew_xpath).click()

    def click_customerinfo(self):
        self.driver.find_element(By.XPATH, self.customer_info_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.text_firstname_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.text_lastname_xpath).send_keys(lastname)

    def select_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdbtn_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdbtn_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdbtn_male_xpath).click()

    def enter_cname(self, cname):
        self.driver.find_element(By.XPATH, self.label_cname_xpath).send_keys(cname)

    def click_texexempt_btn(self):
        self.driver.find_element(By.XPATH, self.taxexempt_xpath).click()

    def select_newsletter(self):
        self.driver.find_element(By.XPATH, self.newsletter_xpath).click()
        self.driver.find_element(By.XPATH, self.select_newspaper_xpath).click()


    def select_customerrole(self, role):
        self.driver.find_element(By.XPATH, self.cusrole_xpath).click()
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.cusrole_guests_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.cusrole_administrators_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.cusrole_forummoderators_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.cusrole_vendors_xpath).click()
        elif role == "Registered":
            pass
        else:
            pass

    def select_manager_vendor(self, vendor):
        drpdown = Select(self.driver.find_element(By.ID, self.managerofvndor_id))
        drpdown.select_by_visible_text(vendor)

    def enter_admin_comment(self, comment):
        self.driver.find_element(By.ID, self.text_admincomment_id).send_keys(comment)

    def click_savebtn(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()



        











