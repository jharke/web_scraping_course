
import requests

url = ('http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/'
       'nama_10_gdp?geo=EU28&precision=1&na_item=B1GQ&unit=CP_MEUR&'
       'time=2010&time=2011')

resp = requests.get(url)
resp_json = resp.json()

resp_json['value']
resp_json['dimension']['time']['category']['index']
