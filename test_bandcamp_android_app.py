from AppPages import SearchPage, SearchResultsPage
import locators

def test_sum(app):
   app_main_page = SearchPage(app)
   app_main_page.click_on_the_search_button(locators.SEARCH_BUTTON_LOCATOR)
   app_main_page.click_on_the_search_button(locators.SEARCH_FIELD_LOCATOR)
   app_main_page.enter_word('Июльские дни', locators.FIELD_TO_ENTER_DATA_LOCATOR)

   result_of_search = SearchResultsPage(app)
   result_of_search.click_group(locators.RESULT_OF_SEARCH_LOCATOR)
   band_location = result_of_search.find_element(locators.BAND_LOCATION_LOCATOR)

   assert band_location.text == 'Nizhny Novgorod, Russia'

