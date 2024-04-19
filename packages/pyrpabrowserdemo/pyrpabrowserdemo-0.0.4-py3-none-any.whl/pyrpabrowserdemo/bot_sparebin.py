from browser import Browser 
from definition import Spreadsheet
import time 


class SpareBinBot:
    def __init__(self):
        self.bot = Browser()
        self.spreadsheet = Spreadsheet()
    
    def run(self):

        self.bot.open_browser('https://robotsparebinindustries.com/')
        self.bot.download_file("https://robotsparebinindustries.com/SalesData.xlsx")

        self.bot.fill_by_id('username', 'maria')
        self.bot.fill_by_id('password', 'thoushallnotpass')

        self.bot.click_general_element('class', 'btn btn-primary')
        time.sleep(5)

        worksheet = self.spreadsheet.get_excel_data('SalesData.xlsx', 'data')
        for row in worksheet:
            self.bot.fill_by_id('firstname', row['First Name'])
            self.bot.fill_by_id('lastname', row['Last Name'])
            self.bot.fill_by_id('salesresult', str(row['Sales Target']))
            self.bot.click_general_element('class', 'btn btn-primary')