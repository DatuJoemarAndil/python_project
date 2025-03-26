from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

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
    print("Test Case 1 - Failed: System Name not found")

# Function to initialize WebDriver
def initialize_driver():
    driver.maximize_window = webdriver.Chrome()
    driver.get_pinned_scripts()
    return driver


# Function to test login functionality
def test_login(driver, username, password):
    driver.get("http://10.10.99.18:8004/login")  # Open login page

    try:
        # Locate Username & Password Fields
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Input Username & Password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click Login Button
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        time.sleep(2)  # Wait for response

        # Check for successful login
        if "dashboard" in driver.current_url:
            print("Login Successful!")
        else:
            print("Login Failed: Invalid credentials or missing fields")
    except NoSuchElementException:
        print("Element not found! Check if the locators are correct.")
    except TimeoutException:
        print("Page took too long to load!")
# Test Cases
driver = initialize_driver()

# Testcase 1: Empty Fields
print("\n🔹 Testcase 1: Empty Login Submission")
test_login(driver, "", "")

# Testcase 2: Invalid Credentials
print("\n🔹 Testcase 2: Invalid Credentials")
test_login(driver, "wrongUser", "wrongPass")

# Testcase 3: Valid Login (Replace with real credentials)
print("\n🔹 Testcase 3: Valid Login")
test_login(driver, "sjjinahon@gmail.com", "Dost@1")
