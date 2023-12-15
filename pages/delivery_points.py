from selenium import webdriver

# Setting to avoid displaying a visible browser window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Create an instance of the Chrome browser
driver = webdriver.Chrome("path_to_chromedriver", options=chrome_options)


def check_delivery_points():
    # Go to the elefant.ro website
    driver.get("https://www.elefant.ro/")

    # Click on the "Delivery Points" link from the main menu
    delivery_points_link = driver.find_element_by_css_selector("li.nav_item:nth-child(3) > a:nth-child(1)")
    delivery_points_link.click()

    # Wait for the page to load completely
    driver.implicitly_wait(5)

    # Check the number of available delivery points
    delivery_points_count = driver.find_element_by_css_selector(".count_b")
    if delivery_points_count.text == "145":
        print("145 delivery points are available.")
    else:
        print("The number of available delivery points is not 145.")


# Call the function to check the delivery points
check_delivery_points()


# Close the browser
driver.quit()