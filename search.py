"""
This module contains AskSearchPage,
the page object for the Ask search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AskSearchPage:
    # URL
    URL = 'https://www.ask.com/'

    # Locators
    SEARCH_INPUT = (By.XPATH, '//*[@id="page"]/header/div/div/div/div[4]/div/form/input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
