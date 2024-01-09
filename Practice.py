import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import xpath
from datetime import datetime,timedelta
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
def filter_buses():
    driver.find_element(By.XPATH,xpath.first_filter_xpath).click()
    time.sleep(3)
    driver.find_element(By.XPATH,xpath.second_filter_xpath).click()
    time.sleep(3)

def select_date():
    month_dates = driver.find_elements(By.XPATH, xpath.month_dates_xpath)
    next_dates = driver.find_elements(By.XPATH, xpath.next_month_dates_xpath)
    import datetime
    current_date = str(datetime.date.today().day)
    current_month_dates = [date.text for date in month_dates]
    next_month_dates = [date.text for date in next_dates]
    try:
        date_after_current_date = current_month_dates.index(current_date) + 2
        month_dates[date_after_current_date].click()
        time.sleep(2)
    except:
        next_dates[1].click()
        time.sleep(2)
    from datetime import datetime
    date_after_2_days_from_current_date = str((datetime.now() + timedelta(days=2)).day)
    date_after_selection= (driver.find_element(By.XPATH,xpath.selected_date_xpath).text).split(' ')[0]
    assert date_after_selection == date_after_2_days_from_current_date

launching_redbus()
selecting_cities()
select_date()
filter_buses()