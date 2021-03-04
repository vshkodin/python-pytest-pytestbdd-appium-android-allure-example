import pytest, allure
from pytest_bdd import scenario, given, when, then
from lib.core.first_page import FirstPage
from lib.tools.getPath import get_path


step_2="Click on button"
step_3="validate middle text"

@scenario(get_path('/tests/bdd/first_page.feature'), 'Login Validation')
def test_login(driver_init, video_recorder):
        """This test for Onboarding"""


@then(step_2)
def step_test_2(driver_init):
    with allure.step(step_2): FirstPage(driver_init).click_on_button()

@then(step_3)
def step_test_3(driver_init):
    with allure.step(step_3): FirstPage(driver_init).validatdate_is_middle_text()
