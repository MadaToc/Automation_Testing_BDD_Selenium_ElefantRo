from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Setting to avoid displaying a visible browser window.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Create an instance of the Chrome browser
driver = webdriver.Chrome("calea_catre_chromedriver", options=chrome_options)


def check_form_submission():
    # Go to the "elefant.ro/corporate" page
    driver.get("https://www.elefant.ro/corporate")

    # Click the "Contact Us Now" link
    contact_link = driver.find_element_by_link_text("Contactează-ne acum")
    contact_link.click()

    # Wait for the page to load completely
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "name")))

    # Fill in the form fields
    name_input = driver.find_element_by_id("name")
    name_input.send_keys("John Doe")

    email_input = driver.find_element_by_id("email")
    email_input.send_keys("johndoe@example.com")

    # Click the submit button
    submit_button = driver.find_element_by_css_selector(".btn-contact-form")
    submit_button.click()

    # Check if the form was not submitted (if the error message is displayed)
    error_message = driver.find_element_by_css_selector(".contact-form-error")
    if error_message.is_displayed():
        print("You cannot submit the form without filling in the required fields.")
    else:
        print("The form was submitted successfully, although the required fields were not filled.")


# Call the function to verify form submission
check_form_submission()

# Close your browser
driver.quit()