from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to initialize WebDriver
def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# Function to log in
def login(driver, username, password):
    driver.get("http://10.10.99.18:8004/login")  # Open login page
    time.sleep(2)

    # Find and fill username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    # Find and fill password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # Click login button
    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    time.sleep(3)  # Wait for login

# Function to navigate to "Applications" and extract data
def navigate_and_extract_applications(driver):
    driver.get("http://10.10.99.18:8004/applications")  # Open Applications page
    time.sleep(3)

    # Extract all rows in the applications table
    applications = driver.find_elements(By.XPATH, "//table/tbody/tr")

    print("\n Extracted Applications:")
    for app in applications:
        columns = app.find_elements(By.TAG_NAME, "td")
        if len(columns) >= 5:
            app_no = columns[0].text
            name = columns[1].text
            engagement = columns[2].text
            institution = columns[3].text
            status = columns[4].text
            print(f" {app_no} | {name} | {engagement} | {institution} | {status}")

# Run automation
driver = initialize_driver()
login(driver, "sjjinahon@gmail.com", "Dost@123")  # Replace with valid credentials
navigate_and_extract_applications(driver)
driver.quit()  # Close browser
