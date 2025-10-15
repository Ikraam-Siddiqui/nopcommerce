import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import LogMaker


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    invalid_email = Read_Config.get_invalid_email()
    logger = LogMaker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("****************test_title_verification started***************************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        if actual_title == expected_title:
            self.logger.info("******************actual title and expected title matched****************************")
            assert True
            self.driver.close()
        else:
            self.logger.info(
                "******************actual title and expected title not matched****************************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self, setup):
        self.logger.info("*******************test_valid_admin_login started****************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.obj_admin_lp = Login_Admin_Page(self.driver)
        self.obj_admin_lp.enter_email(self.email)
        self.obj_admin_lp.enter_password(self.password)
        self.obj_admin_lp.click_login()
        act_dashboard_title = self.driver.find_element(By.XPATH, "//*[contains(@class, 'content-header')]/h1").text
        exp_dashboard_title = "Dashboard"
        if act_dashboard_title == exp_dashboard_title:
            self.logger.info("******************actual dashboard title and expected dashboard title matched****************************")
            assert True
            self.driver.close()
        else:
            self.logger.info("******************actual dashboard title and expected dashboard title not matched****************************")
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
        self.logger.info("******************test_invalid_admin_login started**************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_email(self.invalid_email)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_error_mssg = self.driver.find_element(By.XPATH, "//*[text() = 'No customer account found']").text
        exp_error_mssg = "No customer account found"
        if act_error_mssg == exp_error_mssg:
            assert True
            self.driver.close()
            self.logger.info("*******************Actual error message and expected error message matched**************************")
        else:
            self.logger.info("*******************Actual error message and expected error message not matched**************************")
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False







