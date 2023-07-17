import time
from selenium.webdriver.common.by import By
import datetime as dt

from utils import write_to_xlsx


def get_urls_w(driver, PAGE, LINK_OF_PRODUCTS):
    try:
        while True:
            URL = ('https://www.zara.com/kz/ru/zhenshchiny-rubashki-l1217.html?v1=2290933&page=' + str(PAGE))
            driver.get(URL)
            time.sleep(2)
            wb_search = driver.find_elements(By.CLASS_NAME, 'product-grid-product-info__name')
            if (len(wb_search)):
                for i in wb_search:
                    LINK_OF_PRODUCTS.append(i.get_attribute('href'))
                PAGE += 1
            else:
                break
        print('Все ссылки получены')
    except:
        print("Не могу найти ссылку на товар..")

def get_urls_m(driver, PAGE, LINK_OF_PRODUCTS):
    try:
        while True:
            URL = ('https://www.zara.com/kz/ru/muzhchiny-rubashki-l737.html?v1=2297813&page=' + str(PAGE))
            driver.get(URL)
            time.sleep(2)
            wb_search = driver.find_elements(By.CLASS_NAME, 'product-grid-product-info__name')
            if (len(wb_search)):
                for i in wb_search:
                    LINK_OF_PRODUCTS.append(i.get_attribute('href'))
                PAGE += 1
            else:
                break
        print('Все ссылки получены')
    except:
        print("Не могу найти ссылку на товар..")

def get_attributes(driver, LINK_OF_PRODUCTS, PROPERTIES):
    for link in LINK_OF_PRODUCTS:
        driver.get(link)
        time.sleep(3)
        try:
            nm = driver.find_element(By.CLASS_NAME, 'product-detail-info__header-name')
            price = driver.find_element(By.CLASS_NAME, 'money-amount__main')
            article = driver.find_element(By.CLASS_NAME, 'product-color-extended-name')
            desc = driver.find_element(By.CLASS_NAME, 'expandable-text__inner-content') and driver.find_element(By.TAG_NAME, 'p')
            im = driver.find_element(By.CLASS_NAME, 'media__wrapper--media').get_attribute('src')
            properties = driver.find_elements(By.CLASS_NAME, 'product-detail-extra-detail')
            for i in properties:
                PROPERTIES.append(i.text)
            write_to_xlsx(article.text, nm.text, price.text, desc.text, im, PROPERTIES, link, dt.date.today())
            time.sleep(3)
            PROPERTIES.clear()
        except:
            print("нет атрибута, пропускаю..")