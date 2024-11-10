from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver and open the website
driver = webdriver.Chrome()
driver.get("https://soilhealth.dac.gov.in/home")
wait = WebDriverWait(driver, 120)  # wait up to 20 seconds

# Step 1: Click the Login button
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login_button_id")))  # replace with actual ID for login button
login_button.click()

# Step 2: Select "Central, State, District, STLs" option
central_state_option = wait.until(EC.element_to_be_clickable((By.ID, "central_state_option_id")))  # replace with actual ID
central_state_option.click()

# Step 3: Select User Type = STL and enter username and password
# Locate user type dropdown and select "STL"
user_type_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "user_type_dropdown_id")))  # replace with actual dropdown ID
user_type_dropdown.click()
stl_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='STL']")))  # Use the text "STL" in dropdown
stl_option.click()

# Enter username
username_field = wait.until(EC.presence_of_element_located((By.ID, "username_field_id")))  # replace with actual ID
username_field.send_keys("your_username")

# Enter password
password_field = wait.until(EC.presence_of_element_located((By.ID, "password_field_id")))  # replace with actual ID
password_field.send_keys("your_password")

# Step 4: Submit the form (if there's a submit button, click it; otherwise, you may need to press Enter)
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit_button_id")))  # replace with actual ID for submit
submit_button.click()
