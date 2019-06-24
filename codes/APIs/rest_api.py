
import requests
import pandas as pd

url = ('http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/'
       'nama_10_gdp?geo=EU28&precision=1&na_item=B1GQ&unit=CP_MEUR&'
       'time=2010&time=2011')

resp = requests.get(url)
resp_json = resp.json()

# Get the years that where returned
gdp_years_index = resp_json['dimension']['time']['category']['index']
gdp_years_index

# Get the values that where returned
gdp_value = resp_json['value']
gdp_value

# Function to access certain years value
data = {'Year': list(gdp_years_index.keys()), 'GDP': list(gdp_value.values())}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
df

# Save to csv
df.to_csv('eurostat_gdp.csv')
