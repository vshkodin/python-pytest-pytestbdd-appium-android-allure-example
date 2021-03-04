from appium import webdriver
from lib.tools.getPath import get_path


deviceName = '5758554638573398'
appiumServerUrl = 'http://127.0.0.1:4723/wd/hub'
platformName = 'Android'
deviceDesiredCapabilities = { "deviceName": deviceName,
                            "platformName": platformName,
                            "androidInstallTimeout": 300000,
                              "allowTestPackages": True,
                            "app": get_path("apk/testApp.apk")}



driver = webdriver.Remote(appiumServerUrl, deviceDesiredCapabilities)
driver.implicitly_wait(15)
try:
    driver.find_element_by_accessibility_id('Right').click()
    print(driver.find_element_by_accessibility_id('Center').is_displayed())
    driver.quit()
except:
    driver.quit()
    print(False)