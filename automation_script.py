from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the specified URL
driver.get("https://demoqa.com/automation-practice-form")

# Fill out the form with basic information
driver.find_element_by_id("firstName").send_keys("John")
driver.find_element_by_id("lastName").send_keys("Doe")
driver.find_element_by_id("userEmail").send_keys("john.doe@example.com")
driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
driver.find_element_by_id("userNumber").send_keys("1234567890")
driver.find_element_by_id("dateOfBirthInput").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__month-select']/select").send_keys("January")
driver.find_element_by_xpath("//div[@class='react-datepicker__year-select']/select").send_keys("1990")
driver.find_element_by_xpath("//div[contains(text(),'15')]").click()
assert driver.find_element_by_id("firstName").get_attribute("value") == "John", "First name not filled correctly"
assert driver.find_element_by_id("lastName").get_attribute("value") == "Doe", "Last name not filled correctly"
assert driver.find_element_by_id("userEmail").get_attribute("value") == "john.doe@example.com", "Email not filled correctly"
assert driver.find_element_by_xpath("//label[contains(text(),'Male')]").is_selected(), "Gender not selected correctly"
assert driver.find_element_by_id("userNumber").get_attribute("value") == "1234567890", "Phone number not filled correctly"
assert driver.find_element_by_id("dateOfBirthInput").get_attribute("value") == "15 Jan 1990", "Date of Birth not filled correctly"

# Select subjects
subjects = ["Maths", "Computer Science"]
for subject in subjects:
    driver.find_element_by_id("subjectsInput").send_keys(subject)
    time.sleep(1)
    driver.find_element_by_id("subjectsInput").send_keys(Keys.RETURN)
selected_subjects = driver.find_elements_by_xpath("//div[contains(@class,'selected-subject')]")
assert len(selected_subjects) == len(subjects), "Not all subjects selected"

# Select Hobbies
driver.find_element_by_xpath("//label[contains(text(),'Sports')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Reading')]").click()
selected_hobbies = driver.find_elements_by_xpath("//div[contains(@class,'selected-hobby')]")
assert len(selected_hobbies) == 2, "Not all hobbies selected"

# Upload Picture
driver.find_element_by_id("uploadPicture").send_keys("/path/to/your/picture.jpg")
uploaded_picture = driver.find_element_by_id("uploadedPicture").get_attribute("src")
assert "your/picture.jpg" in uploaded_picture, "Picture not uploaded correctly"

# Fill Address
driver.find_element_by_id("currentAddress").send_keys("123 Street, City, Country")
assert driver.find_element_by_id("currentAddress").get_attribute("value") == "123 Street, City, Country", "Address not filled correctly"

# Select State and City
driver.find_element_by_id("state").click()
driver.find_element_by_xpath("//div[contains(text(),'NCR')]").click()
time.sleep(1)
driver.find_element_by_id("city").click()
driver.find_element_by_xpath("//div[contains(text(),'Delhi')]").click()
assert driver.find_element_by_id("state").get_attribute("value") == "NCR", "State not selected correctly"
assert driver.find_element_by_id("city").get_attribute("value") == "Delhi", "City not selected correctly"

# Submit the form
driver.find_element_by_id("submit").click()
time.sleep(2)  # Wait for the validation message to appear
success_message = driver.find_element_by_xpath("//div[contains(@class,'submit-success')]").text
assert "Thanks for submitting the form" in success_message, "Form submission failed"

# Negative Test Case 1: Submit the form without filling mandatory fields
driver.find_element_by_id("submit").click()
time.sleep(2)  # Wait for the validation message to appear
# Verification Step: Check if the validation message appears for mandatory fields
validation_message = driver.find_element_by_xpath("//div[contains(@class,'text-danger')]").text
assert "This field is required" in validation_message, "Validation message not displayed for mandatory fields"

# Negative Test Case 2: Enter an invalid email address
driver.find_element_by_id("userEmail").clear()
driver.find_element_by_id("userEmail").send_keys("invalid_email")
driver.find_element_by_id("submit").click()
time.sleep(2)  # Wait for the validation message to appear
# Verification Step: Check if the validation message for an invalid email address appears
validation_message = driver.find_element_by_xpath("//div[contains(@class,'text-danger')]").text
assert "Invalid email address" in validation_message, "Validation message for invalid email not displayed"

# Negative Test Case 3: Select more than one gender
driver.find_element_by_xpath("//label[contains(text(),'Female')]").click()
driver.find_element_by_id("submit").click()
time.sleep(2)  # Wait for the validation message to appear
# Verification Step: Check if the validation message for selecting more than one gender appears
validation_message = driver.find_element_by_xpath("//div[contains(@class,'text-danger')]").text
assert "Select only one gender" in validation_message, "Validation message for selecting more than one gender not displayed"

# Negative Test Case 4: Upload an invalid picture format
driver.find_element_by_id("uploadPicture").send_keys("/path/to/invalid_format.txt")
time.sleep(2)  # Wait for the validation message to appear
# Verification Step: Check if the validation message for an invalid picture format appears
validation_message = driver.find_element_by_xpath("//div[contains(@class,'text-danger')]").text
assert "Invalid file format" in validation_message, "Validation message for invalid picture format not displayed"

# Negative Test Case 5: Submit the form with an invalid phone number
driver.find_element_by_id("userNumber").clear()
driver.find_element_by_id("userNumber").send_keys("12345")
driver.find_element_by_id("submit").click()
time.sleep(2)  # Wait for the validation message to appear
# Verification Step: Check if the validation message for an invalid phone number appears
validation_message = driver.find_element_by_xpath("//div[contains(@class,'text-danger')]").text
assert "Invalid phone number" in validation_message, "Validation message for invalid phone number not displayed"

# Close the browser
driver.quit()
