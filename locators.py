from appium.webdriver.common.mobileby import MobileBy


SEARCH_BUTTON_LOCATOR = (MobileBy.ID, "com.bandcamp.android:id/switcher_browse")
SEARCH_FIELD_LOCATOR = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')
FIELD_TO_ENTER_DATA_LOCATOR = (MobileBy.ID, 'com.bandcamp.android:id/search_src_text')
RESULT_OF_SEARCH_LOCATOR = (MobileBy.ID, 'com.bandcamp.android:id/site_search_result_name_band')
BAND_LOCATION_LOCATOR = (MobileBy.ID, 'com.bandcamp.android:id/band_location')
