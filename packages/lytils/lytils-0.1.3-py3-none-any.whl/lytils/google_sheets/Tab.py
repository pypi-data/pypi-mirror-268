# Third-party libraries
from gspread import Worksheet
from gspread_formatting import batch_updater
from gspread_formatting import format_cell_range
from pandas import DataFrame

# Local libraries
from lytils import cprint
from lytils.google_sheets.format import HeaderFormat
from lytils.regex import match
from .Column import Column


# Get column letter from column number.
# 1 = A, 2 = B, ...,  27 = AA, 28 = AB, etc
def get_column_letter(column_number):
    dividend = column_number
    letter = ""
    while dividend > 0:
        remainder = (dividend - 1) % 26
        letter = chr(65 + remainder) + letter
        dividend = (dividend - remainder) // 26
    return letter


# Get column number from column letter.
# A = 1, B = 2, ...,  AA = 27, AB = 28, etc
def get_column_number(column_letter):
    number = 0
    for char in column_letter:
        number = number * 26 + (ord(char) - ord("A") + 1)
    return number


# Get header range from a range in a1 notation
def get_header_range(range: str):
    first_column = match(r"[A-Z]+", range, group=1)
    last_column = match(r"[A-Z]+", range, group=2)
    first_row = match(r"[0-9]+", range, group=1)

    return f"{first_column}{first_row}:{last_column}{first_row}"


# Get data range from a range in a1 notation
def get_data_range(range: str):
    first_column = match(r"[A-Z]+", range, group=1)
    first_row = match(r"[0-9]+", range, group=1)
    last_column = match(r"[A-Z]+", range, group=2)
    last_row = match(r"[0-9]+", range, group=2)

    # Increment first row by 1
    return f"{first_column}{int(first_row) + 1}:{last_column}{last_row}"


class Tab:
    def __init__(self, tab: Worksheet):
        self.__tab = tab
        self.__batch = batch_updater(self.__tab.spreadsheet)

    # Get path in terms of Spreadsheet > Worksheet
    def get_path(self):
        return f"{self.__tab.spreadsheet.title} > {self.__tab.title}"

    # Get all data
    def get_all_data(self) -> DataFrame:
        data = self.__tab.get_values()
        if len(data) > 1:
            return DataFrame(data[1:], columns=data[0])
        else:
            return DataFrame()

    # Get data from specific range
    def get_range(self, range: str, headers: bool = True) -> DataFrame:
        data = self.__tab.get(range)

        if data:
            if headers:
                headers_row = data.pop(0)  # Use the first row as headers
                df = DataFrame(data, columns=headers_row)
            else:
                df = DataFrame(data)
        else:
            df = DataFrame()

        df = df.fillna("")  # Replace None values with an empty string
        return df

    # Clear all data
    def clear(self) -> None:
        self.__tab.clear()

    # Clear specific ranges
    def clear_ranges(self, ranges: list[str]) -> None:
        self.__tab.batch_clear(ranges=ranges)

    # Format single column
    def format_column(self, header, format, header_row=1):
        headers = self.__tab.row_values(header_row)
        header_index = (
            headers.index(header) + 1
        )  # +1 because Google Sheets is 1-indexed
        column_letter = get_column_letter(header_index)
        format_range = f"{column_letter}{header_row + 1}:{column_letter}"
        format_cell_range(self.__tab, format_range, format)

    # Apply formatting to columns
    def format_columns(
        self,
        columns: list[Column],
        column_start: str = "A",
        row_start: int = 2,  # Row starts at 2 to account for headers
    ):
        col_start = get_column_number(column_start)
        formats = []
        for i, col in enumerate(columns, start=col_start):
            column_letter = get_column_letter(i)
            formats.append(
                [
                    f"{column_letter}{row_start}:{column_letter}",
                    col.get_format(),
                ]
            )
        self.__batch.format_cell_ranges(self.__tab, formats)

    # Set desired column widths
    def set_column_widths(self, columns: list[Column], column_start: int = 1):
        widths = []
        for i, col in enumerate(columns, start=column_start):
            column_letter = get_column_letter(i)
            widths.append(
                [
                    f"{column_letter}",
                    col.get_width(),
                ]
            )
        self.__batch.set_column_widths(self.__tab, widths)

    # Clear worksheet and populate with new data. Assumes headers.
    def set_all_data(self, data_frame: DataFrame, columns: list[Column]) -> None:
        self.clear()

        cprint(f"Outputting data to <c>{self.get_path()}<w>...")

        # Correct column order
        order = [col.get_header() for col in columns]
        ordered_df = data_frame[order]

        # Replace NaN with empty string, resulting in empty cells
        df = ordered_df.fillna(value="")

        headers = df.columns.tolist()
        data = df.values.tolist()

        # Format headers
        self.__batch.format_cell_range(self.__tab, "1:1", HeaderFormat())

        # * Format after setting data to include new rows in formatting
        self.format_columns(columns)
        self.set_column_widths(columns)

        # Execute bulk request
        self.__batch.execute()

        # * Formatting has to come BEFORE updates to format correctly

        # Set headers
        self.__tab.update("1:1", [headers])

        # Freeze the top row
        self.__tab.freeze(rows=1)

        # Set data
        self.__tab.update(
            range_name="A2",
            values=data,
            value_input_option="USER_ENTERED",
        )

    # Clear range and set new range with data. Assumes headers.
    def set_range(
        self,
        range: str,
        data_frame: DataFrame,
        columns: list[Column],
    ) -> None:
        cprint(f"Outputting data to <c>{self.get_path()} ({range})<w>...")

        # Correct column order
        order = [col.get_header() for col in columns]
        try:
            ordered_df = data_frame[order]
        except KeyError:
            cprint(f"<y>df columns: {data_frame.columns}")
            cprint(f"<y>order: {order}")
            raise KeyError

        # Replace NaN with empty string, resulting in empty cells
        df = ordered_df.fillna(value="")

        header_range = get_header_range(range)
        data_range = get_data_range(range)

        headers = df.columns.tolist()
        data = df.values.tolist()

        self.clear_ranges(ranges=[range])

        # Format headers
        self.__batch.format_cell_range(self.__tab, header_range, HeaderFormat())

        # * Format after setting data to include new rows in formatting
        column_start = match(r"[A-Z]+", data_range, group=1)
        row_start = match(r"[0-9]+", data_range, group=1)
        self.format_columns(columns, column_start=column_start, row_start=row_start)
        self.set_column_widths(columns, column_start=get_column_number(column_start))

        # Execute bulk request
        self.__batch.execute()

        # * Formatting has to come BEFORE updates to format correctly

        # Set headers
        self.__tab.update(header_range, [headers])

        # Set data
        self.__tab.update(
            range_name=data_range,
            values=data,
            value_input_option="USER_ENTERED",
        )
