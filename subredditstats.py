import demjson
import requests
import pandas as pd
import csv

r = requests.get('https://subredditstats.com/r/soccer')

# json_data = r.text.split('data: ')[1].split('pointSize')[0].strip()[:-1].replace('\n', '')
# growth = demjson.decode(json_data)
# growth_df = pd.DataFrame(growth)
#
# json_data = r.text.split('data: ')[2].split('pointSize')[0].strip()[:-1].replace('\n', '')
# total = demjson.decode(json_data)
# total_df = pd.DataFrame(total)

print(r.text)

# print(total_df)
#
# total_df.to_csv("total_subscribers.csv")
# growth_df.to_csv("subscribers_growth.csv")
