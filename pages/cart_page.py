import time
from selenium.webdriver.common.by import By
from base_page import Base_page

# we make a new class for the cart page, in which we add multiple methods to be called in steps pages
class Cart_page(Base_page): # we import base page, from which we use the needed methods
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[contains(text(), "Adaugă în coș")]')
    ADDED_SUCCESSFULLY_MESSAGE = (By.XPATH, '//*[text() ="Produsul a fost adaugat in cos"]')
    VIEW_BASKET = (By.XPATH, '//*[@id="miniCart"]/div[3]/a')


    def check_url_on_cart_page(self):
        current_url = self.chrome.current_url
        base_url = 'https://www.elefant.ro/'
        product_id = current_url.split('_')[-1].split('.')[0]  # we extract the product identifier from the current URL
        product_name = current_url.split('/')[-1].split('_')[0]  # we extract the product name from the current URL
        expected_url = f'{base_url}{product_name}_{product_id}'  # we construct the expected URL using the base URL, product name, and product identifier
        assert current_url == expected_url, f'ERROR: expected {expected_url}, but got {current_url}' # we verify if the expected url is the same with the actual


    # the following method clicks on the basket
    def click_on_add_to_basket(self):
        self.chrome.find_element(*self.ADD_TO_CART_BUTTON).click()

    # the following method checks the message that appears when we add a product to the cart
    def verify_message_of_added(self,added_to_cart_message):
        time.sleep(4) # I used a sleep here because without it sometimes it would fail, as the HTML loads slow
        self.check_error_message(*self.ADDED_SUCCESSFULLY_MESSAGE, added_to_cart_message)

    # the following method clicks to view the basket
    def view_basket(self):
        self.chrome.find_element(*self.VIEW_BASKET).click()