
import re

with open('test.html') as f:
    html = f.read()

# Find all href tags with http(s) link
links_href = re.findall('href="http[s]?://.*?"', html)

# Find all href tags with http(s) link and return links only
links_only = re.findall('href="(http[s]?://.*?")', html)

# Find all href tags with http(s) link and split
links_parts = re.findall('href="(http[s]?)://(.*?)"', html)
[x[1] for x in links_parts]

# Find all numbers
re.findall('\\d+\\.?\\d?', html)
