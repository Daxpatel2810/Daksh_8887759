# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(8)

# Finding the "Books" department link and clicking on it
bED_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/a/div[1]/div/img")
bED_link.click()


time.sleep(5)

# Finding the "Books" department link and clicking on it
bedd_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/a/img")
bedd_link.click()

# Waiting for the books page to load
time.sleep(5)

# Finding the "Books" department link and clicking on it
bedd1_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/a/img")
bedd1_link.click()

# Waiting for the books page to load
time.sleep(5)

# Finding the "Books" department link and clicking on it
bedd2_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[2]/ul/li[2]/span/div/a/div/div")
bedd2_link.click()

# Waiting for the books page to load
time.sleep(5)



# Verifying that the books page has loaded
assert "Bed" in driver.title



# Adding the book to the cart
add_to_cart_button = driver.find_element("id", "/html/body/div[2]/div/div[5]/div[4]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[16]/div[1]/span/span/span/input")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Proceeding to checkout
proceed_to_checkout = driver.find_element("xpath", "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/form/span/span/span/input")
proceed_to_checkout.click()
time.sleep(2)

# Closing the webdriver
driver.close()
