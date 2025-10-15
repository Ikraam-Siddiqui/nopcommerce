from selenium.webdriver.common.by import By


class Search_Customer_Page():

    # locators for Search page
    email_search_xpath = "//*[@id='SearchEmail']"
    firstname_search_xpath = "//*[@id='SearchFirstName']"
    lastname_search_xpath = "//*[@id='SearchLastName']"
    company_xpath = "//*[@id='SearchCompany']"
    search_btn_xpath = "//button[@id='search-customers']"
    rows_table_xpath = "//table[@id='customers-grid']/tbody/tr"
    columns_table_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_customer_email(self, email):
        self.driver.find_element(By.XPATH, self.email_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_search_xpath).send_keys(email)

    def enter_firstname(self, fname):
        self.driver.find_element(By.XPATH, self.firstname_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstname_search_xpath).send_keys(fname)

    def enter_lastname(self, lname):
        self.driver.find_element(By.XPATH, self.lastname_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastname_search_xpath).send_keys(lname)

    def enter_companyname(self, cname):
        self.driver.find_element(By.XPATH, self.company_xpath).clear()
        self.driver.find_element(By.XPATH, self.company_xpath).send_keys(cname)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()

    def get_results_table_row(self):
        return len(self.driver.find_elements(By.XPATH, self.rows_table_xpath))

    def get_results_table_column(self):
        return len(self.driver.find_elements(By.XPATH, self.columns_table_xpath))

    def search_customer_by_email(self, email):
        email_present_flag = False
        for r in range(1, self.get_results_table_row() + 1):
            cus_email = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text

            if cus_email == email:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_name(self, name):
        name_flag = False
        for r in range(1, self.get_results_table_row() + 1):
            cus_name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text

            if cus_name == name:
                name_flag = True
                break
        return name_flag

    def search_customer_by_cmpname(self, cmpname):
        company_flag = False
        for r in range(1, self.get_results_table_row() + 1):
            cus_company_name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[5]").text

            if cus_company_name == cmpname:
                company_flag = True
                break
        return company_flag




















