from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Set up WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.maximize_window()

# Step 1: Open the website and login
driver.get("https://soilhealth.dac.gov.in/home")

# Input credentials
username = "cvasu248@gmail.com"  # replace with your username
password = "Vasantika@2024"  # replace with your password

# Fill username and password fields
# driver.find_element(By.ID, "username_field_id").send_keys(username)  # replace with actual ID
# driver.find_element(By.ID, "password_field_id").send_keys(password)  # replace with actual ID
# driver.find_element(By.ID, "login_button_id").click()  # replace with actual button ID
print("logged in")


wait = WebDriverWait(driver, 30)  # wait up to 10 seconds

# Step 2: Navigate to Dashboard and select SHC options
username_field = wait.until(EC.presence_of_element_located((By.ID, "username_field_id")))
username_field.send_keys(username)

# Find and fill in the password
password_field = wait.until(EC.presence_of_element_located((By.ID, "password_field_id")))
password_field.send_keys(password)

# Find and click the submit button
submit_field = wait.until(EC.presence_of_element_located((By.ID, "login_button_id")))
submit_field.click()  # Use .click() to submit
# Navigate to SHC page
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SHC"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SHC Completed"))).click()

# Step 3: Fill in dropdowns for District, Block, Village, Language, Cycle, and Scheme
wait.until(EC.presence_of_element_located((By.ID, "district_dropdown_id"))).send_keys("Mahisagar")  # replace with actual ID and selection
wait.until(EC.presence_of_element_located((By.ID, "block_dropdown_id"))).send_keys("VIRPUR - 4165")  # replace with actual ID and selection
wait.until(EC.presence_of_element_located((By.ID, "village_dropdown_id"))).send_keys("Jodhpur - 517308")  # replace with actual ID and selection
wait.until(EC.presence_of_element_located((By.ID, "language_dropdown_id"))).send_keys("ગુજરાતી")  # replace with actual ID and selection
wait.until(EC.presence_of_element_located((By.ID, "cycle_dropdown_id"))).send_keys("2024-25")  # replace with actual ID and selection
wait.until(EC.presence_of_element_located((By.ID, "scheme_dropdown_id"))).send_keys("Soil Health Card RKVY")  # replace with actual ID and selection

# Step 4: Submit the form to get records
driver.find_element(By.ID, "submit_button_id").click()  # replace with actual button ID

# Step 5: Download all records
# Locate download buttons or link and click them in loop
download_buttons = driver.find_elements(By.CLASS_NAME, "download_button_class")  # replace with actual class or selector
for button in download_buttons:
    button.click()
    time.sleep(1)  # Add delay to manage download timing

# Closing the driver after completion
driver.quit()
