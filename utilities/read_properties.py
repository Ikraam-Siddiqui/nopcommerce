import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config():
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_email():
        email = config.get('admin login info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_email():
        invalid_email = config.get('admin login info', 'invalid_email')
        return invalid_email



