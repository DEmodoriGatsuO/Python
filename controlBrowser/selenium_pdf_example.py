import os
path = "***download path***"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": path,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.get("***url***")

#element get & click
