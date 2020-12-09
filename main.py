from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSuiteSettings():
    chromeDriver = webdriver.Chrome()

    def setUp(self):
        return self.chromeDriver

    def tearDown(self):
        self.chromeDriver.close()


class TestData():
    login = "testcaseqa@email.com"
    password = "TestCaseQA"
    userName = "TestCaseQA"
    url = "https://area-dev.sl-int.team/"


def test_main():
    # get test data
    suiteSettings = TestSuiteSettings()
    testData = TestData
    # set chrome driver
    chrome = suiteSettings.setUp()
    chrome.get(testData.url)
    chrome.maximize_window()

    # test 'sign in' button
    WebDriverWait(chrome, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Sign in']"))).click()
    # test login/password
    WebDriverWait(chrome, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='signin-login']"))).send_keys(testData.login)
    chrome.find_element_by_xpath(
        "//input[@id='signin-pass']").send_keys(testData.password)
    chrome.find_element_by_xpath(
        "//button[@type='button' and contains(text(),'Sign in')]").click()

    # test 'username' in menu
    WebDriverWait(chrome, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='userName']")))
    elements = chrome.find_elements_by_xpath(
        "//span[@class='userName' and contains(text(), '{}')]".format(
            testData.userName))
    assert testData.password == elements[0].text

    # test 'plans' button
    WebDriverWait(chrome, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='userName']"))).click()
    WebDriverWait(chrome, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Plans']"))).click()

    # test 'select' button
    WebDriverWait(chrome, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='plan-card__buttons']/div[text()='Select']"))).click()

    suiteSettings.tearDown()
