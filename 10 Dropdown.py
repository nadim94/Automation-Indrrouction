from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)
# Select By Visuable Text
# drp.select_by_visible_text('Morning')

# Select By Index
drp.select_by_index(2)

print(len(drp.options))

all_options = drp.options

for option in all_options:
    print(option.text)