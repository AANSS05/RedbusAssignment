

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
