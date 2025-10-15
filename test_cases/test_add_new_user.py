import pytest
import random
import string
import time
from selenium.webdriver.common.by import By
from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import LogMaker


class Test_03_Add_NewUser:
    admin_page_url = Read_Config.get_admin_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    invalid_email = Read_Config.get_invalid_email()
    logger = LogMaker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self, setup):
        self.logger.info("*********Add new customer started************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.lg_admin = Login_Admin_Page(self.driver)
        self.obj_email = self.lg_admin.enter_email(self.email)
        self.obj_pass = self.lg_admin.enter_password(self.password)
        self.obj_loginbtn = self.lg_admin.click_login()
        self.driver.maximize_window()
        self.logger.info("**********Successfully logged into nopcommerce website*********")
        self.addcustomer = Add_Customer_Page(self.driver)
        self.addcustomer.click_customers()
        self.addcustomer.click_customers_in_menu()
        self.addcustomer.click_addNew()
        self.logger.info("*******Providing customer info started***********")
        email = generate_random_email()
        self.addcustomer.enter_email(email)
        self.addcustomer.enter_password("Test1234")
        self.addcustomer.enter_firstname("Sameer")
        self.addcustomer.enter_lastname("Stark")
        self.addcustomer.select_gender("Male")
        self.addcustomer.enter_cname("InsuredMine")
        self.addcustomer.click_texexempt_btn()
        self.addcustomer.select_newsletter()
        self.addcustomer.select_customerrole("Registered")
        self.addcustomer.select_manager_vendor("Vendor 1")
        self.addcustomer.enter_admin_comment("This customer has been created through automation")
        self.addcustomer.click_savebtn()
        time.sleep(2)
        # test case validation as success message in body text
        customer_add_success_text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']//button[@class='close']")
        customer_text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']//button[@class='close']")

        if customer_add_success_text == customer_text:
            assert True
            self.logger.info("*****************Test_03_Add_NewUser passed*************")
            self.driver.close()
        else:
            self.logger.info("*****************Test_03_Add_NewUser failed*************")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
            self.driver.close()
            assert False















def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # 8 characters username
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']) # choose from the options
    return f'{username}@{domain}'



