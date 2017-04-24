import pandas as pd

json_str = '{"country":"Netherlands","dma_code":"0","timezone":"Europe\/Amsterdam","area_code":"0","ip":"46.19.37.108","asn":"AS196752","continent_code":"EU","isp":"Tilaa V.O.F.","longitude":5.75,"latitude":52.5,"country_code":"NL","country_code3":"NLD"}'

data = pd.read_json(json_str, typ='series')
print "Series\n", data

data["country"] = "Brazil"
print "New Series\n", data.to_json()
