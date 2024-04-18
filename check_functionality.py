from selenium import webdriver
from selenium.webdriver.common.by import By

def ui_test(target):
    try:
        browser = webdriver.Firefox()
        browser.get(target)
        browser.find_element(By.NAME, "firstName").send_keys("test")
        browser.find_element(By.NAME, "lastName").send_keys("test")
        browser.find_element(By.NAME, "phoneNumber").send_keys("123456789")
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
        text = browser.find_element(By.TAG_NAME, "body").text
        print(text)
    except:
        raise("UI test failed")
        
    
    return True

ui_test("http://64.23.209.18//")