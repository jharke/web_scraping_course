
import re
from datetime import datetime

# Date parser for the format twitter API returns
datetime_format = "%a %b %d %H:%M:%S %z %Y"
datetime_format_regex = re.compile(
    r'^\w+\s\w+\s\d{2}\s\d{2}:\d{2}:\d{2}\s\+\d{4}\s\d{4}$'
)


# Datetime parser inspired by https://stackoverflow.com/a/46076215
def datetime_parser(dct):
    for k, v in dct.items():
        if isinstance(v, str) and datetime_format_regex.match(v):
            dct[k] = datetime.strptime(v, datetime_format)
    return dct
