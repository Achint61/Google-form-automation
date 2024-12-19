from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import string
from datetime import datetime

# Correct path to the ChromeDriver executable
CHROMEDRIVER_PATH = "F:/pycharm/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Use consistent forward slashes

# Set up ChromeDriver service and options
service = Service(CHROMEDRIVER_PATH)
options = Options()

# Initialize WebDriver with service and options
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the Google Form URL
    form_url = "https://forms.gle/WT68aV5UnPajeoSc8"
    driver.get(form_url)

    # Wait for the page to load
    time.sleep(2)

    # Fill the input fields (7 input fields, 1 textarea, and 1 date field)
    fields = driver.find_elements(By.XPATH, "//div/input[@class='whsOnd zHQkBf'] | //div/textarea[@class='KHxj8b tL9Q4c']")

    for i, field in enumerate(fields):
        if i == 0:  # First field: Random name
            random_name = ''.join(random.choices(string.ascii_letters, k=8)).capitalize()
            field.send_keys(random_name)
            print(f"Field {i + 1} (Name) filled with: {random_name}")
        elif i == 1:  # Second field: Digit contact number
            contact_number = ''.join(random.choices(string.digits, k=10))
            field.send_keys(contact_number)
            print(f"Field {i + 1} (Contact Number) filled with: {contact_number}")
        elif i == 2:  # Third field: Email ID
            email_id = f"{''.join(random.choices(string.ascii_lowercase, k=5))}@example.com"
            field.send_keys(email_id)
            print(f"Field {i + 1} (Email ID) filled with: {email_id}")
        elif i == 3:  # Fourth field: Full address
            full_address = f"123 Main St, Apt {''.join(random.choices(string.digits, k=3))}, Cityville, Country"
            field.send_keys(full_address)
            print(f"Field {i + 1} (Full Address) filled with: {full_address}")
        elif i == 4:  # Fifth field: Pincode
            pincode = ''.join(random.choices(string.digits, k=6))
            field.send_keys(pincode)
            print(f"Field {i + 1} (Pincode) filled with: {pincode}")
        elif i == 5:  # Sixth field: Date of Birth (DOB)
            dob = "01-01-2003"  # Example DOB
            field.send_keys(dob)
            print(f"Field {i + 1} (Date of Birth) filled with: {dob}")
        elif i == 6:  # Seventh field: Gender
            gender = "Male" or  "Female"  # Example gender; could be "Male" or "Female"
            field.send_keys(gender)
            print(f"Field {i + 1} (Gender) filled with: {gender}")
        elif i == len(fields) - 1:  # Last field: Leave unchanged, but add a specific value
            field.send_keys("GNFPYC")
            print(f"Field {i + 1} (Last Input) filled with: GNFPYC")
        else:
            print(f"Field {i + 1} not handled explicitly.")
        time.sleep(1)  # Optional delay for visibility during execution

    # Locate the specific Submit button using indexing
    submit_buttons = driver.find_elements(By.XPATH, "//span/span[@class='NPEfkd RveJvd snByac']")
    if len(submit_buttons) > 0:
        # Click the first Submit button (index 0)
        submit_buttons[0].click()
        print("Clicked the Submit button.")
    else:
        print("No Submit button found.")

    # Wait for submission to complete and the confirmation page to load
    time.sleep(2)

    # Take a screenshot of the confirmation page
    driver.save_screenshot("confirmation_page.png")
    print("Screenshot saved as confirmation_page.png")

finally:
    # Close the WebDriver
    driver.quit()
