from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import config
from selenium.webdriver.chrome.options import Options



def launch_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(config.chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def launch_app(driver):
    driver.get(config.url)

def close_browser(driver):
    driver.quit()

def get_page_title(driver):
    return driver.title

