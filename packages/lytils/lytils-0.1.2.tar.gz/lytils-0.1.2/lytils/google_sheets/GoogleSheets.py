# Third-party Libraries
import gspread as gs

# Local Libraries
from .Sheet import Sheet


# src: https://practicaldatascience.co.uk/data-science/how-to-read-google-sheets-data-in-pandas-with-gspread
class GoogleSheets:
    # Interface with GoogleSheet API to transform data

    def __init__(self, service_account: str):
        # Authenticate with Google Sheets
        self.__service_account = gs.service_account(filename=service_account)

    def get_sheet(self, url) -> Sheet:
        sheet = self.__service_account.open_by_url(url)
        return Sheet(sheet=sheet)
