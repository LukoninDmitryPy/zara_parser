
from selenium import webdriver

from find import get_urls_w, get_urls_m, get_attributes


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.maximize_window()
    PAGE = 1
    LINK_OF_PRODUCTS = []
    PROPERTIES = []

    try:
        get_urls_w(driver, PAGE, LINK_OF_PRODUCTS)
        get_urls_m(driver, PAGE, LINK_OF_PRODUCTS)
        get_attributes(driver, LINK_OF_PRODUCTS, PROPERTIES)
        
    except Exception as ex:
        print(ex)
        driver.quit()
    driver.quit()

    