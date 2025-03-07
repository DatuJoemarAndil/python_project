from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to open Facebook UI
def open_facebook_ui():
    driver = webdriver.Chrome()  # Open Chrome
    driver.maximize_window()  # Fullscreen window
    driver.get("https://www.facebook.com/")  # Open Facebook

    time.sleep(2)  # Allow time for page load

    # Highlight Username Field
    username_field = driver.find_element(By.NAME, "email")
    username_field.click()
    print("🔹 Clicked Username Field")

    time.sleep(1)

    # Highlight Password Field
    password_field = driver.find_element(By.NAME, "pass")
    password_field.click()
    print("🔹 Clicked Password Field")

    time.sleep(1)

    # Highlight Forgot Password Button
    forgot_password = driver.find_element(By.LINK_TEXT, "Forgotten password?")
    forgot_password.click()
    print("🔹 Clicked 'Forgotten Password?' Link")

    time.sleep(5)  # Observe UI
    driver.quit()  # Close Browser

# Run UI Design Test
open_facebook_ui()
