from appium import webdriver
from lib.tools.getPath import get_path



class Driver:

    def __init__(self, appium_server_url, path_to_apk, step_with_screenshot, device_name):
        deviceDesiredCapabilities = {"deviceName": device_name,
                                     "platformName": 'Android',
                                     "allowTestPackages": True,
                                     "app": get_path(path_to_apk)}
        self.driver = webdriver.Remote(appium_server_url, deviceDesiredCapabilities)
        self.driver.step_with_screenshot = step_with_screenshot
        self.driver.implicitly_wait(15)

    def init_webdriver(self):
        return self.driver

    def quit(self):
        self.driver.quit()
