import time

import pytest

from base_pages.Search_Customer_Page import Search_Customer_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import LogMaker
from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_04_search_element:
    admin_page_url = Read_Config.get_admin_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    invalid_email = Read_Config.get_invalid_email()
    logger = LogMaker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_customer_by_email(self, setup):
        self.logger.info("*********Search customer by email started************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.lg_admin = Login_Admin_Page(self.driver)
        self.obj_email = self.lg_admin.enter_email(self.email)
        self.obj_pass = self.lg_admin.enter_password(self.password)
        self.obj_loginbtn = self.lg_admin.click_login()
        self.driver.maximize_window()
        self.logger.info("**********Successfully logged into nopcommerce website*********")
        self.logger.info("**********Successfully navigated to customer search page*********")
        self.addcustomer = Add_Customer_Page(self.driver)
        self.addcustomer.click_customers()
        self.addcustomer.click_customers_in_menu()
        self.logger.info("**********Starting search customer by email*********")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_email("arthur_holmes@nopCommerce.com")
        self.search_customer.click_search_btn()
        self.logger.info("**********Successfully clicked on search button*********")
        time.sleep(2)
        is_email_present = self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if is_email_present == True:
            assert True
            self.logger.info("**********Test_04_test_search_customer_by_email Passed Successfully*********")
            self.driver.close()
        else:
            self.logger.info("**********Test_04_test_search_customer_by_email Failed*********")
            self.logger.info("**********This email is not present*********")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
            assert False

    def test_search_customer_by_name(self, setup):
        self.logger.info("*********Search customer by name started************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.lg_admin = Login_Admin_Page(self.driver)
        self.obj_email = self.lg_admin.enter_email(self.email)
        self.obj_pass = self.lg_admin.enter_password(self.password)
        self.obj_loginbtn = self.lg_admin.click_login()
        self.driver.maximize_window()
        self.logger.info("**********Successfully logged into nopcommerce website*********")
        self.logger.info("**********Successfully navigated to customer search page*********")
        self.addcustomer = Add_Customer_Page(self.driver)
        self.addcustomer.click_customers()
        self.addcustomer.click_customers_in_menu()
        self.logger.info("**********Starting search customer by name*********")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_firstname("Steve")
        self.search_customer.enter_lastname("Gates")
        self.search_customer.click_search_btn()
        time.sleep(2)
        is_name_present = self.search_customer.search_customer_by_name("Steve Gates")
        if is_name_present == True:
            assert True
            self.logger.info("*********Test_04_search_customer_by_name successfully PASSED**********")
            self.driver.close()
        else:
            self.logger.info("*********Test_04_search_customer_by_name failed**********")
            self.logger.info("**********This name is not present*********")
            self.driver.close()
            assert False

    def test_search_customer_by_company_name(self, setup):
        self.logger.info("*********Search customer by company name started************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.lg_admin = Login_Admin_Page(self.driver)
        self.obj_email = self.lg_admin.enter_email(self.email)
        self.obj_pass = self.lg_admin.enter_password(self.password)
        self.obj_loginbtn = self.lg_admin.click_login()
        self.driver.maximize_window()
        self.logger.info("**********Successfully logged into nopcommerce website*********")
        self.logger.info("**********Successfully navigated to customer search page*********")
        self.addcustomer = Add_Customer_Page(self.driver)
        self.addcustomer.click_customers()
        self.addcustomer.click_customers_in_menu()
        self.logger.info("**********Starting search customer by company name*********")
        self.search_customer.search_customer_by_cmpname("abc private limited")
        self.search_customer.click_search_btn()
        time.sleep(2)
        is_company_name_present = self.search_customer.search_customer_by_cmpname("abc private limited")
        if is_company_name_present == True:
            assert True
            self.logger.info("**********Test_04_search_customer_by_company_name is successfully PASSED*********")
            self.driver.close()
        else:
            self.logger.info("**********Test_04_search_customer_by_company_name is failed*********")
            self.logger.info("**********This Company name is not present*********")
            self.driver.close()
            assert False











