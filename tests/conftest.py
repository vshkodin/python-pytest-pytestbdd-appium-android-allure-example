import allure, os, pytest
from lib.tools.videoRecorder import VideoRecorder
from lib.fixtures.driver_init_fixture import Driver
from pytest_bdd import scenario, given, when, then

web_driver, test_name = None, None

def pytest_addoption(parser):
    parser.addoption('--appium_server_url', action='store', dest='appium_server_url')
    parser.addoption('--device_name', action='store', dest='device_name')
    parser.addoption('--path_to_apk', action='store', dest='path_to_apk')
    parser.addoption('--video_recorder', action='store', dest='video_recorder')
    parser.addoption('--step_with_screenshot', action='store', dest='step_with_screenshot')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        web_driver.save_screenshot("ERROR.png")
        allure.attach.file("ERROR.png", attachment_type=allure.attachment_type.PNG, name='ERROR')
        os.system('rm -f ' + "ERROR.png ")


@pytest.fixture(scope="session")
def driver_init(request):
    global web_driver
    web_driver = Driver(
                            request.config.getoption('appium_server_url'),
                            request.config.getoption('path_to_apk'),
                            request.config.getoption('step_with_screenshot'),
                            request.config.getoption('device_name')
                        )
    web_driver = web_driver.init_webdriver()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def video_recorder(request):
    recorder = VideoRecorder(web_driver, request.config.getoption('video_recorder'))
    test_name = request.node.name
    yield recorder
    recorder.stop_recording(test_name)

@given("I'm a Tester")
def step_test_1():
    with allure.step("I'm a Tester"): pass