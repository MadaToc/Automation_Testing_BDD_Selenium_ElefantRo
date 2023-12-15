import time
from selenium.webdriver.common.by import By
from browser import Browser

# we make a new class for the main page, in which we add multiple methods to be called in steps pages
class Main_Page(Browser):
    SEARCH_BAR = (By.XPATH, '//*[@id="HeaderRow"]/div[4]/div/div[1]/form/input[1]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button')

    # this method takes us to the main page
    def navigate_to_main_page(self):
        self.chrome.get('https://www.elefant.ro/')
        time.sleep(3) # the cookies might take a while to load into the HTML, so I use a sleep of 3 sec. (yes, I could've used an explicit wait, but that would make the code longer)
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()  # this clicks on the cookies accept
        except:
            pass # here we used try/except because the cookies agreement won't appear after we first accept them or might not appear at all


    # this method clicks on the wanted element
    def click_on_main_page_elements(self, element):
        time.sleep(1) # I gave it an extra sleep of one sec to let the HTML code load
        self.chrome.find_element(By.XPATH, element).click()

    # this method verifies the page url using an assert
    def check_page_url(self, page):
        current_url = self.chrome.current_url
        assert page == current_url , f'Error, expected page url {page} but got {current_url}'

    # this method checks that we see the success_text while we are on the wanted page
    def check_success_text(self, success_text, text_element):
        actual_text = self.chrome.find_element(By.XPATH, text_element).text
        assert success_text == actual_text, f'Expected text {success_text}, but got {actual_text}'

    # this method adds on the search bar the text from 'product' and then clicks on the SEARCH_BUTTON
    def search_for_product(self, product):
        self.chrome.find_element(*self.SEARCH_BAR).send_keys(product)
        self.chrome.find_element(*self.SEARCH_BUTTON).click()