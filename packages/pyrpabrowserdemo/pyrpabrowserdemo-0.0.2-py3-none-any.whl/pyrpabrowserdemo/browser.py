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

        | Input Text When Element Is Visible | //input[@id="freetext"]  | my feedback |
        """
        self.fill(f'//*[@id="{id}"]', field)