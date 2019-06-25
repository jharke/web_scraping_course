
import re
import requests

url = "https://www.ebay-kleinanzeigen.de/s-gewerbeimmobilien/berlin/c277l3331"
r = requests.get(url)
html = r.text

# Find all href tags with http(s) link
re.findall('href="https?://.*?"', html)

# Find all href tags with http(s) link and return links only
re.findall('href="(https?://.*?)"', html)

# Find all href tags with http(s) link and split
links_parts = re.findall('href="(https?)://(.*?)"', html)
[x[0] for x in links_parts]
[x[1] for x in links_parts]

# Find all prices
prices = re.findall('(\\d+(\\.?\\d+)*,?\\d*\\s€)', html)
prices = [x[0] for x in prices]
prices

# Clean up all prices
prices_clean = [re.sub('[^(\\d,)]', '', x) for x in prices]
prices_clean

# Greedy matching example

# Keep in mind that regex dot <b>.</b> does not match line terminators
# like <b>\n</b>.

string = '<div class="conditionalcomment-outcomeboxbody"><p>Du verwendest derzeit eine alte Version des Internet Explorers. eBay Kleinanzeigen funktioniert besser, wenn du einen <a class="lnk-action" href="https://www.mozilla.org/de/firefox/new/" target="_blank">aktuellen Browser installierst</a>.</p></div>\n This is a new line. As the regex dot . does not match line terminators like \n this part should not be returned in any example below. '

# Use greedy matching (without " at the end)
re.findall('href="https?://.*', string)

# Use non-greedy matching (without " at the end)
re.findall('href="https?://.*?', string)

# But what we actually want to get is the non-greedy matching followed
# by " at the end.
re.findall('href="https?://.*?"', string)
