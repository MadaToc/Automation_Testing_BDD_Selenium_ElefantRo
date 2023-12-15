"""
This module contains AskResultPage,
the page object for the AskPage search result page.
"""

from selenium.webdriver.common.by import By


class AskResultPage:

  # Locators

  RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
  SEARCH_INPUT = (By.XPATH, '//*[@id="page"]/header/div/div/div/div[4]/div/form/input')

  # Initializer
  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  def result_link_titles(self):
    links = self.browser.find_elements(*self.RESULT_LINKS)
    titles = [link.text for link in links]
    return titles

  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    value = search_input.get_attribute('value')
    return value

  def title(self):
    return self.browser.title