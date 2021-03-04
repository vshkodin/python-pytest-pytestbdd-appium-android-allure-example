import allure, os, time
from tests.conftest import test_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class SharedDriverClass:

    def __init__(self, driver):
        self.driver = driver

    def _driver_find_element_by(self, element, by):
        if by == "ID": return self.driver.find_element_by_id(element)
        elif by == "AI": return self.driver.find_element_by_accessibility_id(element)
        elif by == "XP": return self.driver.find_element_by_xpath(element)

    def _driver_find_elements_by(self, element, by):
        if by == "ID": return self.driver.find_elements_by_id(element)
        elif by == "AI": return self.driver.find_elements_by_accessibility_id(element)
        elif by == "XP": return self.driver.find_elements_by_xpath(element)

    @allure.step('Validating text')
    def _validate_text(self, elem, text, by):
        validate = (self._driver_find_element_by(elem, by).text)
        validate = validate.replace('\n',' ')
        assert validate == text
        self._take_screenshot_validate_text(text)

    @allure.step('Click through grid')
    def _click_through_grid(self, elem, by):
        grid = (self._driver_find_elements_by(elem, by))
        for i in grid:
            i.click()
            self._take_screenshot_click()

    @allure.step('Clicking On')
    def _click(self, elem, by):
        target = self._driver_find_element_by(elem, by)
        target.click()
        self._take_screenshot_click()  # TODO refactor method

    @allure.step('Send text')
    def _send(self, elem, string, by):
        target=(self._driver_find_element_by(elem,by))
        target.send_keys(string)
        self._take_screenshot_click()

    @allure.step('Click on element from the Grid')
    def _click_grid_element(self, elements, gridNum, by):
        time.sleep(.5)
        grid = (self._driver_find_elements_by(elements,by))
        grid[gridNum].click()
        self._take_screenshot_click()

    @allure.step('Click Back phone button')
    def _button_back(self):
        time.sleep(2)
        self.driver.back()
        self._take_screenshot_click()

    @allure.step('Close Android Keyboard')
    def _close_keyboard(self):
        self.driver.hide_keyboard()

    @allure.step('Swipe from one location to another using coordinates')
    def _swipe_from_coordinates(self, x1, y1, x2, y2, num_loops, wait_time):
        for i in range(num_loops):
            action = TouchAction(self.driver)
            action.press(x=x1, y=y1)
            action.wait(wait_time)
            action.move_to(x=x2, y=y2)
            action.release()
            action.perform()
        self._take_screenshot_click()

    @allure.step('Press a particular key on an Android Device keyboard')
    def _press_keyboard(self, keycode):
        self.driver.press_keycode(keycode)
        self._take_screenshot_click()

    def _take_screenshot_click(self):
        if self.driver.step_with_screenshot=="True":
            self.driver.save_screenshot(str(test_name) + ".png")
            allure.attach.file(str(test_name) + ".png", attachment_type=allure.attachment_type.PNG)
            os.system('rm -f ' + str(test_name) + ".png ")
        else:
            pass


    @allure.step('is displayed')
    def _isDisplayed(self, elem, by):
        target = self._driver_find_element_by(elem,by)
        assert True == target.is_displayed()
        self._take_screenshot_click()  # TODO refactor method

    def _wait_till_present(self,elem_wait):
        WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.ID, elem_wait)))

    @allure.step('Scroll to button')
    def _scroll_to_button(self, first_element):  # TODO  Refactor required
        action = TouchAction(self.driver)
        el = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, first_element)))
        action.press(el).move_to(x=10, y=-3000).release().perform()

    def _take_screenshot_validate_text(self, text):
        if self.driver.step_with_screenshot=="True":
            self.driver.save_screenshot(str(test_name) + ".png")
            allure.attach.file(str(test_name) + ".png", attachment_type=allure.attachment_type.PNG,
                               name='Validating text = '+str(text))
            os.system('rm -f ' + str(test_name) + ".png ")
        else:
            pass

    @allure.step('Send text and wait')
    def _send_and_wait(self, elem, string, elem_wait):
        self.driver.find_element_by_id(elem).send_keys(string)
        self._wait_till_present(elem_wait)
        self._take_screenshot_click()

    @allure.step('Open a deep link')
    def _open_deep_link(self, url):
        self.driver.get(url)
        self._take_screenshot_click()

    def _wait_till_present_class(self, elem_wait):
        WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, elem_wait)))

    def _waiting(self,sec):
        time.sleep(int(sec))
        self._take_screenshot_click()

