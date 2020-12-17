from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def web_driver_wait_element_clickable(driver, time, locator):
    return WebDriverWait(driver, int(time)).until(
        EC.element_to_be_clickable(
            (By.XPATH, str(locator))))


def web_driver_wait_element_located(driver, time, locator):
    return WebDriverWait(driver, int(time)).until(
        EC.presence_of_element_located(
            (By.XPATH, str(locator))))