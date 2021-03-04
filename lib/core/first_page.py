from lib.locators import first_page as locator
from lib.core.sharedDriver import SharedDriverClass
import allure


class FirstPage:

    def __init__(self, driver): self.shared_driver = SharedDriverClass(driver)

    @allure.step('Clicking through Stores')
    def click_on_button(self):
        self.shared_driver._click(locator.button, by='AI')

    @allure.step('Clicking through Stores')
    def validatdate_is_middle_text(self):
        self.shared_driver._isDisplayed(locator.MiddleText, by="AI")
