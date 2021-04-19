from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
directory ="C:/Users/Md. Nadim Kaysar/Downloads/New folder"
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": r"C:\Users\Md. Nadim Kaysar\Downloads\New folder",
    # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": False,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
})

driver = webdriver.Chrome(executable_path="C:/Drivers/newchrom/chromedriver.exe", options=options)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element_by_id("textbox").send_keys("ABCD")
time.sleep(2)
driver.find_element_by_id("createTxt").click()
time.sleep(2)
driver.find_element_by_id("link-to-download").click()
