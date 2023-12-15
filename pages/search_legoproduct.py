from selenium import webdriver

# Setarea pentru a evita afișarea unei ferestre de browser vizibile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Create an instance of the Chrome browser
driver = webdriver.Chrome("path_to_chromedriver", options=chrome_options)


def search_and_check_lego():
    search_term = "lego"  # The LEGO search term

    # Go to the elefant.ro website
    driver.get("https://www.elefant.ro/")

    # Enter your search criteria in the search bar
    search_input = driver.find_element_by_id("search_box")
    search_input.send_keys(search_term)

    # Click the search button
    search_button = driver.find_element_by_css_selector(".submit_search")
    search_button.click()

    # Apply sorting by relevance
    relevance_sort_option = driver.find_element_by_css_selector(".sort_type select option[value='relevanta']")
    relevance_sort_option.click()

    # Check if the first product in the list is LEGO
    first_product = driver.find_element_by_css_selector(".product_name")
    if "LEGO" in first_product.text:
        print("The first product on the list is LEGO.")
    else:
        print("The first product on the list is not LEGO.")


# Call the function to search and check the LEGO product
search_and_check_lego()

# Close your browser
driver.quit()