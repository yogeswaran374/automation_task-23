from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#initializing the driver & URL
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

#finding element

driver.switch_to.frame(0)

dragable_element=driver.find_element(By.XPATH, "//div[@id='draggable']")
dropable_element=driver.find_element(By.XPATH, "//div[@id='droppable']")

#do actions for drag & drop

actions = ActionChains(driver)
actions.drag_and_drop(dragable_element,dropable_element).perform()
time.sleep(5)

