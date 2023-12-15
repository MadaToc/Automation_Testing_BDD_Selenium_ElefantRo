from base_page import Base_page
import time
from selenium.webdriver.common.by import By

# we make a new class for the login page, in which we add multiple methods to be called in steps pages
class Login_page(Base_page):
    EMAIL = (By.XPATH, '//*[@id="ShopLoginForm_Login"]')
    PASSWORD = (By.XPATH, '//*[@id="ShopLoginForm_Password"]')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button')
    ERROR_MESSAGE_INVALID_EMAIL = (By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[1]/div/small[1]')
    ERROR_MESSAGE_WRONG_EMAIL = (By.XPATH, '/html/body/div[3]/div/div[9]/div[1]/div/div[1]/div/div')


    # this method takes us to the login page
    def navigate_to_login_page(self):
        self.chrome.get('https://www.elefant.ro/login')


    # this method sends an email to the path provided in EMAIL
    def insert_email(self, email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)


    # this method sends a password to the path provided in PASSWORD
    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)


    # this method clicks on the login button
    def login_button_click(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()


    # this method verifies the email errors
    def check_login_error(self, error_message):
        time.sleep(3) # necessary to allow the website to fully load before checking for the current URL.
        current_url = self.chrome.current_url
        expected_url = "https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessLogin"
        if current_url == expected_url:
            self.check_error_message(*self.ERROR_MESSAGE_WRONG_EMAIL, error_message) # when providing an incorrect email (i.e. faffaff@gmggddg.com) the site will at first try to login,
                                                                                        # but then send us to a new page with the expected_url, where we will see the error ERROR_MESSAGE_WRONG_EMAIL
        else:
            self.check_error_message(*self.ERROR_MESSAGE_INVALID_EMAIL, error_message) # in case we write an invalid email (i.e. afafdf) or without an '@' we get this error 'ERROR_MESSAGE_INVALID_EMAIL'


    # in this method we inset a specific email that we know has an account
    def insert_specific_email(self):
        self.chrome.find_element(*self.EMAIL).send_keys('JohnyNebunu@mail.com')


    # here we insert the correct password
    def insert_specific_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('DacaMaiBeauUnPahar')
    # sadly, there is no captcha and the page should have a captcha for security reasons


    # this method verifies that we are actually logged in, by verifying the page expected url and title
    def verify_url_and_title(self):
        actual_title = self.chrome.title
        expected_title = 'Contul Meu'
        assert expected_title == actual_title, f'Expected {expected_title}, but got title {actual_title}'
        actual_url = self.chrome.current_url
        expected_url = 'https://www.elefant.ro/my-account?TrackingDataContainerID='
        assert expected_url == actual_url, f'We are not on the {expected_url}, instead we are on {actual_url}'