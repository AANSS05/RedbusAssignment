import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import xpath

application_url = 'https://www.redbus.in/'

def launching_redbus():
    global driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(application_url)

def selecting_cities():
    driver.find_element(By.XPATH, xpath.from_source_field_xpath).send_keys('Mumbai')
    time.sleep(2)
    From_cities_suggestion_list = driver.find_elements(By.XPATH, xpath.from_cities_suggestion_xpath)
    for city in From_cities_suggestion_list:
        try :
            if city.text == 'Borivali East':
                city.click()
                time.sleep(2)
        except:
            pass
    driver.find_element(By.ID,"dest").send_keys('Bangalore')
    time.sleep(2)
    Destination_cities_suggestion_list = driver.find_elements(By.XPATH, xpath.destination_cities_suggestion_xpath)
    for city in Destination_cities_suggestion_list:
        try:
            if city.text == 'Indiranagar':
                city.click()
                time.sleep(2)
        except:
            pass

