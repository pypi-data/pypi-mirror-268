from gspread import Spreadsheet
from .Tab import Tab

class Sheet:
    def __init__(self, sheet: Spreadsheet):
        self.__sheet = sheet

    def get_tab(self, name: str) -> Tab:
        tab = self.__sheet.worksheet(name)
        return Tab(tab=tab)
