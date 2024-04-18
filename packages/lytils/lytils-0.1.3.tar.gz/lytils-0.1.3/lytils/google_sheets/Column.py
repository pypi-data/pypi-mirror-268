# Third-party libraries
from gspread_formatting import CellFormat

# Local libraries
from .format import DefaultFormat


class Column:
    def __init__(
        self,
        header: str,
        format: CellFormat = DefaultFormat(),
        width: int = 100,
    ):
        self.__header = header
        self.__format = format
        self.__width = width

    def get_header(self):
        return self.__header

    def get_format(self):
        return self.__format

    def get_width(self):
        return self.__width
