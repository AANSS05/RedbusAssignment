def filter_buses():
    driver.find_element(By.XPATH,xpath.first_filter_xpath).click()
    time.sleep(3)
    driver.find_element(By.XPATH,xpath.second_filter_xpath).click()
    time.sleep(3)
