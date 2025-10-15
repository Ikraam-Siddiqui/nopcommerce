import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import LogMaker
from utilities import excel_utils


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = LogMaker.log_gen()
    path = ".//test_data//admin_login_data.xlsx"
    status_list = []

    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("*******************test_valid_admin_login_data_driven started****************************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.obj_admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, 'Sheet1')
        print("Number of rows:", self.rows)

        for r in range(2, self.rows+1):
            self.email = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.obj_admin_lp.enter_email(self.email)
            self.obj_admin_lp.enter_password(self.password)
            self.obj_admin_lp.click_login()
            time.sleep(5)
            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.exp_login == "Yes":
                    self.status_list.append("Pass")
                    self.logger.info("Test data is passed")
                    self.obj_admin_lp.click_logout()
                elif self.exp_login == "No":
                    self.status_list.append("Fail")
                    self.logger.info("Test data is failed")
                    self.obj_admin_lp.click_logout()

            if actual_title != exp_title:
                if self.exp_login == "Yes":
                    self.status_list.append("Fail")
                    self.logger.info("Test data is failed")
                if self.exp_login == "No":
                    self.status_list.append("Pass")
                    self.logger.info("Test data is passed")

        print("Status list is: ", self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven is failed")
            assert False
        else:
            self.logger.info("Test admin data driven is passed")
            assert True














