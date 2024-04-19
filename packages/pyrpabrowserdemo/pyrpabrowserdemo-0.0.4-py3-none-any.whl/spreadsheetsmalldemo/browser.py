from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP


class Browser():
    def __init__(self):
        self.browser = Selenium()
    
    def open_browser(self, url: str) -> None:
        self.browser.open_available_browser(url)

    def change_to_frame(self, frame_xpath: str) -> None:
        self.browser.unselect_frame()
        self.browser.wait_until_element_is_visible(frame_xpath, timeout=60 * 2)
        iframe = self.browser.find_element(frame_xpath)
        self.browser.select_frame(iframe)

    def select_frame(self, frame_xpath: str) -> None:
        self.browser.select_frame(frame_xpath)

    def download_file(self, url: str) -> None:
        http = HTTP()
        http.download(url)