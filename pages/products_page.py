from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from base_page import Base_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# we make a new class for the products page, in which we add multiple methods to be called in steps pages
class Products_page(Base_page):
    OUT_OF_STOCK = (By.XPATH, '//*[text()="Stoc epuizat!"]')

    # this method checks that the product name is in the search results
    def verify_results_contain_product_text(self, search_results, product):
        results_list = self.chrome.find_elements(By.XPATH, search_results)
        for i in range(5):
            results = results_list[i].text.lower().replace('ă', 'a').replace('ț', 't').replace('î','i').replace('â', 'a').replace('ș','s').replace('Ă','A').replace('Ț','T').replace('Î','I').replace('Â','A').replace('Ș','S')
            # we use the replace method on those  special characters from the romanian alphabet because otherwise I would receive an UnicodeEncode error, and the HTML report would not be generated
            assert product in results, f'Error, Product {product} does not appear in {results} at product number {i}'
            # this assert might fail because the site elefant also adds in the search results promoted products that have no correlation to the search input

    # this method clicks on the product
    def click_on_the_product(self, search_results):
        self.chrome.implicitly_wait(0)  # we disable implicit wait temporarily
        wait = WebDriverWait(self.chrome, 10)  # we define an explicit wait of 10 seconds
        results_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, search_results))) # I had issues with implicit wait, so here we are using explicit wait
        if len(results_list) >= 2:
            try:
                results_list[1].click()
            except ElementClickInterceptedException: # in case the product is out of stock there will be a layer over the product and the said elements we want to click, therefore we call this Exception
                overlay_element = self.chrome.find_element(*self.OUT_OF_STOCK)
                if overlay_element.is_displayed():
                    raise Exception("PRODUCT OUT OF STOCK") # in case the product is out of stock we raise this error and stop the tests regarding that product
        else:
            raise ValueError("Expected at least 2 search results, but found fewer.")