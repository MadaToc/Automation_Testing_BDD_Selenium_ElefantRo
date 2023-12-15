from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # we rename expected_conditions as EC for better use in the code
import time
from selenium.webdriver.common.by import By
from base_page import Base_page
import random
from selenium.webdriver.common.action_chains import ActionChains


# we make a new class for the account creation page, in which we add multiple methods to be called in steps pages
class Create_Account(Base_page):
    SURNAME = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_FirstName"]')
    NAME = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_LastName"]')
    EMAIL = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_Login"]')
    EMAIL_ERROR = (By.XPATH, '//*[text()="Adresa de e-mail nu este corectă"]')
    PASSWORD = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_Password"]')
    REPEAT_PASSWORD = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_RetypedPassword"]')
    PASSWORD_ERROR = (By.XPATH, '//*[text()="Parolele nu coincid"]')
    ALL_PREFERENCES = (By.XPATH, '//*[@id="selectAll"]')
    CREATE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[9]/div[3]/div/div/form/div[9]/div') #//*[text()="Creează cont"]
    AGREEMENT = (By.XPATH, '//*[@id="PostCheckoutRegisterForm_TermsAndConditions"]')
    NEWSLETTER_NOTIFICATION= (By.XPATH, '/html/body/div[1]//div/button/svg/path[2]')
    GENDER = (By.XPATH, '//input[@type = "radio"]')
    USER_ALREADY_EXISTS = (By.XPATH, '//body/div[2]/div/div[9]/div[3]/div/div/div/div')

    # this method takes us to the account creation page
    def navigate_to_create_account_page(self):
        self.chrome.get('https://www.elefant.ro/new-account?TargetPipeline=ViewProfileSettings-ViewProfile')


    def choose_status(self):
        action = ActionChains(self.chrome)
        gender_elements = self.chrome.find_elements(*self.GENDER)
        selected_gender_index = random.randint(0, len(gender_elements) - 1)
        selected_gender_element = gender_elements[selected_gender_index]
        action.move_to_element(selected_gender_element)
        action.click()
        action.perform()
        # we are also using action chains to click on the radio buttons
        # using random lib, this method randomly chooses the status/gender


    # this method sends the surname value to the surname from the page
    # we are using a parametrized surname because we used scenario outline in the feature and this way we make the code more efficient
    def insert_new_surname(self, surname):
        self.chrome.find_element(*self.SURNAME).send_keys(surname)


    # this method sends the name value to the surname from the page
    # we are using a parametrized name because we used scenario outline in the feature and this way we make the code more efficient
    def insert_new_name(self, name):
        self.chrome.find_element(*self.NAME).send_keys(name)


    # this method sends the email value to the surname from the page
    # we are using a parametrized email because we used scenario outline in the feature and this way we make the code more efficient
    def insert_new_email(self, email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)


    # this method first checks if the error is displayed
    # then using the check_error_message from base page, checks the email error
    def check_mail_error(self, error_message):
        time.sleep(3)  # using a sleep of 3 seconds prevents the code from failing as the page loads, we also save some lines of code by not needing to put an explicit wait
        is_error_displayed = self.chrome.find_element(*self.EMAIL_ERROR).is_displayed()
        if is_error_displayed:
            self.check_error_message(*self.EMAIL_ERROR, error_message)


    # this method sends the email value to the surname from the page
    # we are using a parametrized email because we used scenario outline in the feature and this way we make the code more efficient
    # it also sends the same password to the repeat password part
    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)
        self.chrome.find_element(*self.REPEAT_PASSWORD).send_keys(password)


    # in the case the repeated password this method will return an error
    # to be more specific, in case the password from REPEAT_PASSWORD does not match the password from PASSWORD
    def password_error(self, error_message):
        time.sleep(3) # using a sleep of 3 seconds prevents the code from failing as the page loads, we also save some lines of code by not needing to put an explicit wait
        is_error_displayed = self.chrome.find_element(*self.PASSWORD_ERROR).is_displayed()
        if is_error_displayed: # this checks if the error is displayed
            self.check_error_message(*self.PASSWORD_ERROR, error_message)


    # this method checks all preferences using action chains lib
    # we are using action chains because the simple .clik() method won't work
    def click_on_all_preferences(self):
        action = ActionChains(self.chrome)
        radio_button = self.chrome.find_element(*self.ALL_PREFERENCES)
        action.move_to_element(radio_button)
        action.click()
        action.perform()

    # this method clicks on agree using action chains lib
    # we are using action chains because the simple .clik() method won't work
    def click_on_agreement(self):
        action = ActionChains(self.chrome)
        radio_button =self.chrome.find_element(*self.AGREEMENT)
        action.move_to_element(radio_button)
        action.click()
        action.perform()

    def click_create_account(self):
        self.chrome.implicitly_wait(0)  # we disable implicit wait temporarily
        wait = WebDriverWait(self.chrome, 10)  # we define an explicit wait of 10 seconds
        button = wait.until(EC.visibility_of_element_located(self.CREATE_BUTTON))
        self.chrome.execute_script("arguments[0].scrollIntoView();", button) # we scroll into the view of the create button
        button.click() # we click the button

    # this method verifies the error in case the user already exists
    # we also use the check_error_message from base page
    def check_create_account_error(self, error_message):
        self.check_error_message(*self.USER_ALREADY_EXISTS, error_message)
'''
when we add special characters to the name or surname at first the site will accept them, but afterwards it will return an error
when we will be sent to another page where an error alert/box will appear but with no actual error inside it
when the site appears to not accept numbers as the surname, but accepts numbers as the name
then when inserting special characters we finally receive the errors, this error is in english even though the others are in romanian
'''