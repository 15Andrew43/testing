import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=200x300')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()




def test_title(browser):
    browser.get("http://localhost:8080")

    assert 'DostavimVse' == browser.title


def test_orderhistory(browser):
    browser.get("http://localhost:8080")

    browser.find_element(By.ID, 'get-order-history').click()
    assert 'Getting Started: Serving Web Content' == browser.title

    browser.find_element(By.ID, 'main-page').click()
    assert 'DostavimVse' == browser.title


def test_orderpage(browser):
    browser.get("http://localhost:8080")

    browser.find_element(By.ID, 'create-order-button').click()
    assert 'Get Legs Test' == browser.title

    browser.find_element(By.ID, 'receiver-id').send_keys('1')
    browser.find_element(By.ID, 'start-vertex-id').send_keys('2')
    browser.find_element(By.ID, 'end-vertex-id').send_keys('3')
    browser.find_element(By.CLASS_NAME, 'weight-input').send_keys('4')
    browser.find_element(By.CLASS_NAME, 'price-input').send_keys('5')
    browser.find_element(By.ID, 'send-order').click()

    time.sleep(1)

    cur_order_id = browser.find_element(By.XPATH, "/html/body/div[@class='order-info']/div[1]/span").text

    browser.find_element(By.ID, 'main-page').click()
    assert 'DostavimVse' == browser.title

    # browser.find_element(By.ID, 'get-order-history').click()

    # time.sleep(1)
    # assert 'Getting Started: Serving Web Content' == browser.title

    # for elem in browser.find_elements(By.XPATH, "/html/body/table[1]/tbody[1]/tr"):
    #     button = elem.find_element(By.XPATH, "./td/a")
    #     if button.text == cur_order_id:
    #         button.click()
    #         time.sleep(4)



def test_findorder(browser):
    browser.get("http://localhost:8080")

    browser.find_element(By.ID, 'get-order-input').send_keys('1')
    browser.find_element(By.ID, 'get-order-button').click()

    browser.find_element(By.ID, 'main-page').click()
    assert 'DostavimVse' == browser.title
