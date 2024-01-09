import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import xpath
from xpath import *
import datetime
from datetime import datetime,timedelta



def bus_with_low_fare():
    driver.find_element(By.XPATH, xpath.Fare_link_xpath).click()
    elements = driver.find_elements(By.XPATH, xpath.All_buses_details_xpath)
    buses = [item.text for item in elements]
    low_fare_bus = buses[0]
    bus = [item for item in low_fare_bus.split('\n')]
    for details in bus:
        if details.startswith('INR'):
            print(bus[0]+' has the lowest fair of '+details)


bus_with_low_fare()
