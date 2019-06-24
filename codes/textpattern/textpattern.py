
import re
import requests

url = "https://www.ebay-kleinanzeigen.de/s-gewerbeimmobilien/berlin/c277l3331"
r = requests.get(url)
html = r.text

# Find all href tags with http(s) link
re.findall('href="http[s]?://.*?"', html)

# Find all href tags with http(s) link and return links only
re.findall('href="(http[s]?://.*?")', html)

# Find all href tags with http(s) link and split
links_parts = re.findall('href="(http[s]?)://(.*?)"', html)
[x[1] for x in links_parts]

# Find all prices
prices = re.findall('\\d+\\.?\\d+\\s?€', html)
prices

# Clean up all prices
prices_clean = [re.sub('[^\\d]', '', x) for x in prices]
prices_clean
