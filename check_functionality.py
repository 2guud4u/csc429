import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def ui_test(target):
    try:
        browser = webdriver.Firefox()
        browser.get(target)
        time.sleep(5)
        browser.find_element(By.NAME, "firstName").send_keys("test")
        browser.find_element(By.NAME, "lastName").send_keys("test")
        browser.find_element(By.NAME, "phoneNumber").send_keys("123456789")
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
        text = browser.find_element(By.TAG_NAME, "body").text
        if "Order Submitted Successfully. Your transaction ID is:" not in text:
            print("UI test failed")
            raise "UI test failed"
    except Exception as e:
        print("UI test failed in except block", e)
        raise("UI test failed")
    
