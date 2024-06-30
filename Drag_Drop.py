from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable and droppable elements
frame = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(frame)

# Locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Create an ActionChains object
actions = ActionChains(driver)

# Perform the drag and drop operation
actions.drag_and_drop(draggable, droppable).perform()


dropped_text = droppable.text
if dropped_text == "Dropped!":
    print("Drag and drop successful!")
else:
    print("Drag and drop failed.")

# Close the browser window
driver.quit()
