from gspread_formatting import CellFormat
from gspread_formatting import NumberFormat as GSNumberFormat
from gspread_formatting import TextFormat as GSTextFormat


def DefaultFormat() -> CellFormat:
    return CellFormat(
        numberFormat=GSNumberFormat(type="NUMBER", pattern="General"),
        verticalAlignment="TOP",
    )


def HeaderFormat(**kwargs) -> CellFormat:
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                textFormat=GSTextFormat(bold=True),
                **kwargs,
            ),
        ]
    )


def DateTimeFormat(pattern="yyyy-mm-dd hh:mm:ss", **kwargs) -> CellFormat:
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                numberFormat=GSNumberFormat(type="DATE_TIME", pattern=pattern),
                **kwargs,
            ),
        ]
    )


def TimeFormat(pattern: str = "hh:mm:ss", **kwargs) -> CellFormat:
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                numberFormat=GSNumberFormat(type="TIME", pattern=pattern),
                **kwargs,
            ),
        ]
    )


def AccountingFormat(**kwargs) -> CellFormat:
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                numberFormat=GSNumberFormat(
                    type="NUMBER",
                    pattern='_("$"* #,##0.00_);_("$"* \(#,##0.00\);_("$"* "-"??_);_(@_)',
                ),
                **kwargs,
            ),
        ]
    )


def NumberFormat(pattern="0", **kwargs) -> CellFormat:
    # Possible patterns:
    # "0" -> 1234
    # "0.00" -> 1234.00
    # "#,##0" -> 1,234
    # "#,##0.00" -> 1,234.00
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                numberFormat=GSNumberFormat(type="NUMBER", pattern=pattern),
                **kwargs,
            ),
        ]
    )


def TextFormat(**kwargs) -> CellFormat:
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                numberFormat=GSNumberFormat(type="TEXT", pattern="@"),
                horizontalAlignment="LEFT",
                **kwargs,
            ),
        ]
    )


def WrapTextFormat(**kwargs) -> CellFormat:
    return merge_cell_formats(
        [
            DefaultFormat(),
            CellFormat(
                numberFormat=GSNumberFormat(type="TEXT", pattern="@"),
                horizontalAlignment="LEFT",
                wrapStrategy="WRAP",
                **kwargs,
            ),
        ]
    )


def merge_cell_formats(formats) -> CellFormat:
    """Merges a list of CellFormat objects into a single CellFormat object.

    Args:
        formats: A list of CellFormat objects.
        [format1, format2, format3]: In the case of similar properties,
            format2 will take priority over format1, and format3 will take
            priority over format1 and format2.

    Returns:
        A CellFormat object that contains the properties of all of the input objects.
    """
    merged_format = CellFormat()
    for format in formats:
        for property_name, property_value in format.__dict__.items():
            if not hasattr(merged_format, property_name):
                setattr(merged_format, property_name, property_value)
            elif property_value != merged_format.__dict__[property_name]:
                setattr(merged_format, property_name, property_value)

    return merged_format
