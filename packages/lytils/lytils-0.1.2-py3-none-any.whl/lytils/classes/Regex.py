import re

# Defines regex functions
class Regex:
    def apply(regex, text):
        new_text = text
        if regex['type'] == 'match':
            new_text = Regex.match(regex, new_text)
        elif regex['type'] == 'replace':
            new_text = Regex.replace(regex, new_text)
        return new_text
    def match(regex, text):
        find = re.search(regex['pattern'], text)
        return find.group() if find else ''
    def replace(regex, text):
        return re.sub(
            regex['old_value'],
            regex['new_value'],
            text
        )

# Defines regex Types
class RegexType:
    def match(pattern):
        return {
            'type': 'match',
            'pattern': pattern
        }
    def replace(old_value, new_value):
        return {
            'type': 'replace',
            'old_value': old_value,
            'new_value': new_value
        }