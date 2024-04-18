import pandas as pd
from lytils.regex import replace


def convert_accounting_to_numeric(column: pd.Series):
    def transform_column(text: str) -> float:
        text = replace(r"[\$,-]", "", text).strip()
        return float(text) if text != "" else 0

    return column.apply(transform_column)
