from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP


class Browser():
    def __init__(self):
        self.browser = Selenium()
    
    def open_browser(self, url: str) -> None:
        """
        Open available browser
        """
        self.browser.open_available_browser(url)
        self.browser.maximize_browser_window()

    def change_to_frame(self, frame_xpath: str) -> None:
        """
        Unselect the current frame and select the new frame.
        """
        self.browser.unselect_frame()
        self.browser.wait_until_element_is_visible(frame_xpath, timeout=60 * 2)
        iframe = self.browser.find_element(frame_xpath)
        self.browser.select_frame(iframe)

    def select_frame(self, frame_xpath: str) -> None:
        """
        Select iframe element by xpath.
        """
        self.browser.select_frame(frame_xpath)

    def download_file(self, url: str) -> None:
        """
        An alias for the ``HTTP Get`` keyword.
        """
        http = HTTP()
        http.download(url)

    def fill(self, locator: str, field: str) -> None:
         """
         Input text into locator after it has become visible.

        ``locator`` element locator

        ``field`` insert text to locator

        Example:

        | Input Text When Element Is Visible | //input[@id="freetext"]  | my feedback |
        """
         self.browser.input_text_when_element_is_visible(locator, field)

    def click_by_aria_label(self, label: str) -> None:
        aria_label = f'//button[@aria-label="{label}"]'
        self.browser.wait_and_click_button(aria_label)

    def select_table_frame_value(self, table_frame: str, value_locator: str) -> None:
        """
        Select a table frame and click on it's value.
        """
        self.browser.select_frame(table_frame)
        self.browser.wait_until_element_is_visible(value_locator)
        table_value = self.browser.find_element(value_locator)
        table_value.click()

    def click(self, xpath: str) -> None:
        """
        Click on element by xpath.
        """
        self.browser.wait_until_element_is_visible(xpath, timeout=60 * 2)
        element = self.browser.find_element(xpath)
        element.click()

    def fill_by_id(self, id: str, field: str) -> None:
        """
        Input text into locator after it has become visible.

        ``id`` element locator

        ``field`` insert text to locator

        Example:

        | Input text when id element is available | //input[@id="freetext"]
        """
        self.fill(f'//*[@id="{id}"]', field)

    
    def click_element_by_data_test_id(self, locator: str) -> None:
        """
        Find element by data-test-id.
        """
        self.browser.wait_until_element_is_visible(f'//*[@data-testid="{locator}"]')
        element = self.browser.find_element(f'//*[@data-testid="{locator}"]')
        element.click()

    def get_element_by_data_test_id(self, locator: str) -> None:
        """
        Find element by data-test-id.
        """
        self.browser.wait_until_element_is_visible(f'//*[@data-testid="{locator}"]')
        element = self.browser.find_element(f'//*[@data-testid="{locator}"]')
        return element
    
    def get_elements_by_data_test_id(self, locator: str) -> None:
        """
        Find elements by data-test-id.
        """
        self.browser.wait_until_element_is_visible(f'//*[@data-testid="{locator}"]')
        elements = self.browser.find_elements(f'//*[@data-testid="{locator}"]')
        return elements
    
    def get_text_by_data_test_id(self, locator: str) -> None:
        """
        Get text from element by data-test-id.
        """
        try:
            self.browser.wait_until_element_is_visible(f'//*[@data-testid="{locator}"]')
            element = self.browser.find_element(f'//*[@data-testid="{locator}"]')
            return element.text
        except Exception as e:
            print(e)
            
    def get_webelements_by_id(self, id: str) -> None:
        """
        Get elements by id.
        """
        self.browser.wait_until_element_is_visible(f'//*[@id="{id}"]')
        elements = self.browser.find_elements(f'//*[@id="{id}"]')
        return elements

    def click_general_element(self, html_element_name: str, value: str) -> None:
        """
        Get as general element the string f'//*[@{html_element_name}="{value}"]'
        Wait until element is visible and click on it.
        """
       
        self.browser.wait_until_element_is_visible(f'//*[@{html_element_name}="{value}"]')
        element = self.browser.find_element(f'//*[@{html_element_name}="{value}"]')
        element.click()

    def click_button_by_type(self, type: str) -> None:
        """
        Click on button by type.
        """
        #//*[button[@type="submit"]]
        self.browser.wait_until_element_is_enabled(f'//*[button[@type="{type}"]]')
        self.browser.click_element_when_clickable(f'//*[button[@type="{type}"]]')

    def click_by_text(self, web_elements, text: str) -> None:
        """
        Click on element by text.
        """
        for web_element in web_elements:
            if text in web_element.text:
                web_element.click()



    #Sign in or register