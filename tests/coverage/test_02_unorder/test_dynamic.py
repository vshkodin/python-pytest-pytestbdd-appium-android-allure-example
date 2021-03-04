from pytest_bdd import scenarios, given, then, parsers
import pytest, allure, time
from lib.tools.getPath import get_path
from lib.core.sharedDriver import SharedDriverClass


scenarios((get_path('tests/bdd/unordered')))
# TODO implement video recorder


@then(parsers.parse('Tap on "{LOCATOR}", By "{BY}"'))
def click_on_by(driver_init, LOCATOR, BY):
    with allure.step(f"Tap BY : {BY} LOCATOR: {LOCATOR}"):
        SharedDriverClass(driver_init)._click(LOCATOR,BY)


@then(parsers.parse('Validate element is presented "{LOCATOR}", By "{BY}"'))
def validate_displayed(driver_init, LOCATOR, BY):
    with allure.step(f'Validate element is presented LOCATOR : {LOCATOR}, By : {BY}'):
        SharedDriverClass(driver_init)._isDisplayed(LOCATOR, BY)


@then(parsers.parse('In field "{LOCATOR}" type "{STRING}", By "{BY}"'))
def send_keys(driver_init, LOCATOR, BY, STRING):
    with allure.step(f"Send Keys by : {BY} LOCATOR: {LOCATOR}  TYPE : {STRING}"):
        SharedDriverClass(driver_init)._send(LOCATOR, STRING, BY)


@then(parsers.parse('Validate text "{LOCATOR}", "{STRING}", By "{BY}"'))
def validate_text(driver_init,LOCATOR, BY, STRING):
    with allure.step(f'Validate text LOCATOR : {LOCATOR}, STRING : {STRING}, By  : {BY}'):
        SharedDriverClass(driver_init)._validate_text(LOCATOR, STRING, BY)


@then(parsers.parse('Wait "{SEC}"'))
def _time_wait(driver_init,SEC):
    with allure.step(f'Wait "{SEC}"'):
        SharedDriverClass(driver_init)._waiting(SEC)


@then(parsers.parse('Open a deep link "{URL}"'))
def _time_wait(driver_init,URL):
    with allure.step(f'link "{URL}"'):
        SharedDriverClass(driver_init)._open_deep_link(URL)
