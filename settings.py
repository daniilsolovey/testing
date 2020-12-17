class UserData():
    login = "testcaseqa@email.com"
    password = "TestCaseQA"
    name = "TestCaseQA"


class Locators():
    base_url = "https://area-dev.sl-int.team/"
    sign_in_btn = "//a[text()='Sign in']"
    sign_in_login_filed = "//input[@id='signin-login']"
    sign_in_password_field = "//input[@id='signin-pass']"
    sign_in_submit_button = "//button[@type='button' and contains(text(),'Sign in')]"
    user_name_tab = "//span[@class='userName']"
    user_name_btn = "//span[@class='userName' and contains(text(), '{}')]".format(UserData.name)
    plans_btn = "//a[text()='Plans']"
    select_btn = "//div[@class='plan-card__buttons']/div[text()='Select']"
