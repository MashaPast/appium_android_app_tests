import pytest
from appium import webdriver
from selenium.webdriver.common.by import By


def test_sum():

   capabilities = {
       'platformName': 'Android',
       'deviceName': 'Genymotion Cloud PaaS',
       'appPackage': 'com.bandcamp.android',
       'appActivity': '.root.RootActivity',
       #'automationName': 'UiAutomator2',
       #'noReset': True,
   }
   url = 'http://localhost:4723/wd/hub'
   driver = webdriver.Remote(url, capabilities)

   try:
       search_button = driver.find_element(By.ID, "com.bandcamp.android:id/switcher_browse")
       search_button.click()

       search_field = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')
       search_field.click()

       field_to_enter_data = driver.find_element(By.ID, 'com.bandcamp.android:id/search_src_text')
       field_to_enter_data.send_keys("Июльские дни")

       result_of_search = driver.find_element(By.ID, 'com.bandcamp.android:id/site_search_result_name_band')
       result_of_search.click()

       driver.implicitly_wait(5)


       band_location = driver.find_element(By.ID, 'com.bandcamp.android:id/band_location')
       print(band_location)

       assert band_location.text == 'Nizhny Novgorod, Russia'

   finally:
       # teardown appium
        driver.quit()