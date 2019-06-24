
import re
import requests
import datetime


# Get src of url and add to
def url_add_src(page, url_base, url_prefix, url_suffix, init_src=''):
    url = url_base + url_prefix + str(page) + url_suffix
    r = requests.get(url)
    init_src += r.text
    return init_src


src = ''
for i in range(1, 10 + 1):
    src = url_add_src(i,
                      'https://www.ebay-kleinanzeigen.de/',
                      's-gewerbeimmobilien/berlin/seite:',
                      '/c277l3331',
                      src)

# Find all prices
prices = re.findall('<strong>(\\d+\\.?\\d+\\s?€)</strong>', src)
prices

# Clean up all prices
prices_clean = [re.sub('[^\\d]', '', x) for x in prices]
prices_clean

# Find all dates in the format Day.Month.Year
dates = re.findall('\\d{2}\\.\\d{2}\\.\\d{4}', src)
dates

# Convert in pythons datetime format
dates_py_format = [datetime.datetime.strptime(i, '%d.%m.%Y') for i in dates]
dates_py_format


# Advanced: Find all dates including todays and yesterday entries
dates = re.findall('[A-Za-z]{5,7}, \\d{2}:\\d{2}|\\d{2}\\.\\d{2}\\.\\d{4}', src)


def replace_day_string(dates_list, day_string, new_date):
    repl = [re.sub(day_string + ', \\d{2}:\\d{2}',
                   '.'.join([f"{new_date:%d}",
                             f"{new_date:%m}",
                             f"{new_date:%Y}"]), x) for x in dates_list]
    return repl


# Replace "Heute"
dates = replace_day_string(dates, 'Heute', datetime.datetime.now())

# Replace "Gestern"
dates = replace_day_string(dates,
                           'Gestern',
                           datetime.datetime.now() - datetime.timedelta(days=1))

# Print result
dates

# Convert in pythons datetime format
dates_py_format = [datetime.datetime.strptime(i, '%d.%m.%Y') for i in dates]
dates_py_format
