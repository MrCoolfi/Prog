from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_wildberries_items():
    driver = webdriver.Chrome()
    driver.get("https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA%D0%B8")
    time.sleep(10)
    
    items = []
    products = driver.find_elements(By.CLASS_NAME, "product-card")[:40]
    
    for product in products:
        try:
            title = product.find_element(By.CLASS_NAME, "product-card__name").text.strip()
            price = product.find_element(By.CLASS_NAME, "price__lower-price").text
            items.append({
                "title": title[1:] if title.startswith('/') else title,
                "price": float(price.replace('₽', '').replace(' ', '')),
                "rating": 4
            })
        except:
            continue
            
    driver.quit()
    return items