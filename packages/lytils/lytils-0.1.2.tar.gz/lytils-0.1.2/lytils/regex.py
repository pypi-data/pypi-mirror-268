from re import finditer, search, sub


# @param: group (int): Get first group, second group, etc. 1-based.
def match(regex: str, text: str, group: int = 1) -> str:
    matches = list(finditer(regex, text))
    try:
        return matches[group - 1].group(0)
    except IndexError:
        return ""


def replace(regex: str, replace_with: str, text: str) -> str:
    return sub(regex, replace_with, text)
