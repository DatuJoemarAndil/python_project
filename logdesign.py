from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Website Link
Website_link = "http://10.10.99.18:8004/login"
driver.get(Website_link)

# Test Case 1: View System Name
try:
    system_name_element = driver.find_element(By.XPATH,
                                              "//h1[@class='font-brush text-center text-4xl lg:text-6xl text-shadow-sm text-heading-blue']")
    system_name_text = system_name_element.text.strip()

    expected_text = "Balik Scientist Program Management System"

    if system_name_text == expected_text:
        print("Test Case 1 - Passed")
    else:
        print(f"Test Case 1 - Failed; Expected: '{expected_text}', Found: '{system_name_text}'")
except NoSuchElementException:
    print("Test Case 1 - Failed: System Name was not found")

# Close the browser
driver.quit()