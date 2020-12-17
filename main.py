import settings
from time import sleep
import keywords


def test_main(driver):
    """
    test login page, user tab, plans button, select button, sign_in button
    """
    locators = settings.Locators
    user = settings.UserData
    driver.get(locators.base_url)
    sleep(1)

    keywords.web_driver_wait_element_clickable(driver, 20, locators.sign_in_btn).click()
    # test login/password
    keywords.web_driver_wait_element_clickable(
        driver, 20, locators.sign_in_login_filed,
        ).send_keys(user.login)

    driver.find_element_by_xpath(
        locators.sign_in_password_field).send_keys(user.password)
    driver.find_element_by_xpath(
        locators.sign_in_submit_button).click()

    # test 'username' in menu
    keywords.web_driver_wait_element_located(driver, 20, locators.user_name_tab)
    elements = driver.find_elements_by_xpath(locators.user_name_btn)
    assert user.password == elements[0].text

    # test 'plans' button
    keywords.web_driver_wait_element_clickable(driver, 20, locators.user_name_tab).click()
    keywords.web_driver_wait_element_clickable(driver, 20, locators.plans_btn).click()

    # test 'select' button
    keywords.web_driver_wait_element_clickable(driver, 20, locators.select_btn).click()
