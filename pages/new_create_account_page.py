import time
from selenium.webdriver.common.by import By
from base_page import Base_page


# we make a new class for the account creation page that we are being sent after writing special characters and trying to create an account, in which we add multiple methods to be called in steps pages
class New_Create_Account_Page(Base_page):
    BOX_ERROR = (By.XPATH, '/html/body/div[3]/div/div[9]/div[3]/div/div/div')
    SURNAME = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_FirstName"]')
    NAME = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_LastName"]')
    SURNAME_ERROR = (By.XPATH, '/html/body/div[3]/div/div[9]/div[3]/div/div/form/div[2]/div/small[3]')
    NAME_ERROR = (By.XPATH, '/html/body/div[3]/div/div[9]/div[3]/div/div/form/div[3]/div/small[3]')


    # this method verifies the url
    def check_url(self):
        time.sleep(3)
        actual_url = self.chrome.current_url
        expected_url = 'https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessRegisterUserSimple'
        assert expected_url == actual_url, f'ERROR, I am not on the correct page'

    # this method checks that the error is first displayed and that it has no text in it
    # the error we first get just appears to be a red box with no text in it
    def assert_element_has_text(self):
        time.sleep(3)
        element = self.chrome.find_element(*self.BOX_ERROR)
        if element.is_displayed():
            assert element.text == False, f"The error box contains text"

    # we again add special characters to the SURNAME and NAME paths
    def add_special_characters_to_surname_and_name(self):
        self.chrome.find_element(*self.SURNAME).send_keys('$#$#$#')
        self.chrome.find_element(*self.NAME).send_keys('-%&*&$#')

    # we verify that the error is now present
    def verify_special_char_error(self, error_message):
        self.check_error_message(*self.SURNAME_ERROR, error_message)
        self.check_error_message(*self.NAME_ERROR, error_message)