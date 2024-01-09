def scroll_up():
    driver.execute_script("window.scrollTo(0,100)")

def click_on_search_button():
    driver.find_element(By.XPATH,xpath.search_button_xpath).click()
