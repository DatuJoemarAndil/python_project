from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
website_link = "http://10.10.99.18:8003/online-application"
driver.get(website_link)

# Wait for the page to load
time.sleep(3)

# Test Case 1: Verify Page Title
try:
    page_title = driver.find_element(By.XPATH, "//h2[contains(text(), 'Online Application Registration Form')]")
    print("Test Case 1 - Passed: Page title is correct")
except NoSuchElementException:
    print("Test Case 1 - Failed: Page title not found")
