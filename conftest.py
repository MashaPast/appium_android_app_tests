import pytest
from appium import webdriver


@pytest.fixture()
def app():
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'Genymotion Cloud PaaS',
        'appPackage': 'com.bandcamp.android',
        'appActivity': '.root.RootActivity',
        # 'automationName': 'UiAutomator2',
        # 'noReset': True,
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    yield driver
    driver.quit()