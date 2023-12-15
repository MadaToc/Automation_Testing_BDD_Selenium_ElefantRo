from base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # we rename expected_conditions as EC for better use in the code

# we make a new class for the checkout page, in which we add multiple methods to be called in steps pages
class Checkout_page(Base_page):
    REMOVE_FROM_BASKET = (By.XPATH, '//*[text()="cancel"]')
    NO_PRODUCT_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div[10]/h2')
    CONTINUE_SHOPPING = (By.XPATH, '/html/body/div[2]/div/div[10]/a')


    def remove_from_basket(self):
        self.chrome.implicitly_wait(0)  # we disable implicit wait temporarily
        wait = WebDriverWait(self.chrome, 10)  # we define an explicit wait of 10 seconds
        remove = wait.until(EC.presence_of_all_elements_located(self.REMOVE_FROM_BASKET)) # we add the explicit wait because the implicit wait fails as the HTML DOM does not appear instantly
        remove[3].click() # on the HTML we click on the third element

    # in the following method, using the check_error_message from base page we verify the message that we receive when removing the product from the cart
    def verify_no_product_message(self, removed_from_cart_message):
        self.check_error_message(*self.NO_PRODUCT_MESSAGE, removed_from_cart_message)

    # in the following method, we click on the continue shopping button
    def click_on_continue_shopping(self):
        self.chrome.find_element(*self.CONTINUE_SHOPPING).click()