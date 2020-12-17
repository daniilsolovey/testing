import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    chrome_driver.close()
