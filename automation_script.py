from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the specified URL
driver.get("https://demoqa.com/automation-practice-form")

# Test Case 1: Fill out the form with basic information
driver.find_element_by_id("firstName").send_keys("John")
driver.find_element_by_id("lastName").send_keys("Doe")
driver.find_element_by_id("userEmail").send_keys("john.doe@example.com")
driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
driver.find_element_by_id("userNumber").send_keys("1234567890")
driver.find_element_by_id("dateOfBirthInput").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__month-select']/select").send_keys("January")
driver.find_element_by_xpath("//div[@class='react-datepicker__year-select']/select").send_keys("1990")
driver.find_element_by_xpath("//div[contains(text(),'15')]").click()

# Test Case 2: Select subjects
subjects = ["Maths", "Computer Science"]
for subject in subjects:
    driver.find_element_by_id("subjectsInput").send_keys(subject)
    time.sleep(1)
    driver.find_element_by_id("subjectsInput").send_keys(Keys.RETURN)

# Test Case 3: Select Hobbies
driver.find_element_by_xpath("//label[contains(text(),'Sports')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Reading')]").click()

# Test Case 4: Upload Picture
driver.find_element_by_id("uploadPicture").send_keys("/path/to/your/picture.jpg")

# Test Case 5: Fill Address
driver.find_element_by_id("currentAddress").send_keys("123 Street, City, Country")

# Test Case 6: Select State and City
driver.find_element_by_id("state").click()
driver.find_element_by_xpath("//div[contains(text(),'NCR')]").click()
time.sleep(1)
driver.find_element_by_id("city").click()
driver.find_element_by_xpath("//div[contains(text(),'Delhi')]").click()

# Test Case 7: Submit the form
driver.find_element_by_id("submit").click()

# Wait for a few seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()
