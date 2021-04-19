from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
# OpenPyXl need to install for this
import openpyxl

path = "C:/Users/Md. Nadim Kaysar/Downloads/New folder/test2.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active  # workbook.get_sheet_names("sheet1")

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value="welcome"
workbook.save(path)
