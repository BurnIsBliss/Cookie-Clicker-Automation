import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://orteil.dashnet.org/cookieclicker/v10466/')
wait.until(ec.element_to_be_clickable((By.ID, 'bigCookie')))
bigCookie = driver.find_element(By.ID, 'bigCookie')
while True:
    # Getting the list of available products for purchase
    availableProducts = driver.find_elements(By.XPATH,"//div[@id='products']/div[contains(@class,'enabled')]")

    # Getting the list of available upgrades for purchase
    availableUpgrades = driver.find_elements(By.CSS_SELECTOR, '#upgrade0.enabled')

    # Checking if there are any available upgrades
    if len(availableUpgrades):
        availableUpgrades[0].click()

        # using the sleep method to avoid flakiness
        time.sleep(0.5)

    # Checking if there are any available products for upgrade
    elif len(availableProducts):
        availableProducts[0].click()
    bigCookie.click()