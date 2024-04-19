from RPA.HTTP import HTTP
from RPA.Excel.Files import Files
import pandas as pd
import os

class Spreadsheet:
    def __init__(self):
        pass

    def get_dataframe_filtered(self, file_path: str, sheet_name: str, column: str, value: str):
        dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
        filtered_dataframe = dataframe[dataframe[column] == value]
        return filtered_dataframe
    
    def check_file_exists(self, file_path: str):
        if os.path.exists(file_path):
            return True
        return False
    
    def convert_list_to_excel(self, list_to_df: list, file_path: str) -> None:
        """
        list_to_df: list of dictionaries
        file_path: directory and file format
        """
        df = pd.DataFrame(list_to_df)
        df.to_excel(file_path, index=False)

    def download_file(self, url: str) -> None:
        """
        An alias for the ``HTTP Get`` keyword.
        """
        http = HTTP()
        http.download(url)

    def get_excel_data(self, excel_file_name: str, spreadsheet_name: str):
        """Read data from excel and fill in the sales form"""
        excel = Files()
        excel.open_workbook(excel_file_name)
        worksheet = excel.read_worksheet_as_table(spreadsheet_name, header=True)
        return worksheet


    
