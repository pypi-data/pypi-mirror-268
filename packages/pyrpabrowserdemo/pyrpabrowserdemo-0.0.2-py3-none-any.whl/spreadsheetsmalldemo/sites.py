from abc import ABC
from RPA.Browser.Selenium import Selenium



class Sites(ABC):
    def __init___(self):
        self.browser = Selenium()