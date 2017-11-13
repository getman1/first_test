from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("https://duckduckgo.com/")

delay = 3 #seconds waiting for browser upload next page

search_field = driver.find_element_by_id("search_form_input_homepage")

search_field.send_keys("Iaroslav Getman")

link = driver.find_element_by_id("search_button_homepage")

link.click()

load_more_button = driver.find_element_by_class_name("result--more__btn");
actions = ActionChains(driver)
actions.move_to_element(load_more_button).perform()

third_page = driver.find_element_by_id("rld-2");
actions = ActionChains(driver)
actions.move_to_element(third_page).perform()

find_second_page_second_link = driver.find_element_by_id("r1-32")
find_second_page_second_link.click()





"""
# find_element = driver.find_element_by_id('#rld-1')
# wait = WebDriverWait(driver, 60)

# obj = wait.until(EC.presence_of_element_located((find_element)))
# element.location_once_scrolled_into_view

# scroll load button

# scroll to selector #rld-1

# find element under rld-1 apropriate link 
"""

