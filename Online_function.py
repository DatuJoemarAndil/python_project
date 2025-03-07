from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


# Function to initialize WebDriver
def initialize_driver():
    driver.maximize_window = webdriver.Chrome()
    driver()
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
            print("✅ Login Successful!")
        else:
            print("❌ Login Failed: Invalid credentials or missing fields")
    except NoSuchElementException:
        print("⚠️ Element not found! Check if the locators are correct.")
    except TimeoutException:
        print("⏳ Page took too long to load!")
    finally:
        driver.quit()  # Close browser


# Test Cases
driver = initialize_driver()

# Test 1: Empty Fields
print("\n🔹 Test 1: Empty Login Submission")
test_login(driver, "", "")

# Test 2: Invalid Credentials
print("\n🔹 Test 2: Invalid Credentials")
test_login(driver, "wrongUser", "wrongPass")

# Test 3: Valid Login (Replace with real credentials)
print("\n🔹 Test 3: Valid Login")
test_login(driver, "admin", "admin123")
