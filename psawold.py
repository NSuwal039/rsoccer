import datetime
import csv
import json
import requests

def getPushshiftData(ini_date,end_date):
    url = 'https://api.pushshift.io/reddit/search/submission/?&size=500&after='+ini_date+'&before='+end_date+'&subreddit=soccer'  # 2015 before christmas
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']

def retrievedata(dataset, filename, modec):
    with open(filename+'.csv', modec, newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if modec=='w':
            writer.writerow(['title', 'author', 'score', 'domain', 'url', 'num_comments', 'created_utc', 'selftext'])

        for i in dataset:
            writer.writerow(
                [i['title'], i['author'], i['score'], i['domain'], i['url'], i['num_comments'], i['created_utc'],
                 i['selftext']])

filereader = open('2013dates.csv','r')
csvreader = csv.reader(filereader)

col_num = len(next(csvreader))

for row in csvreader:
    print(row)
    resultarray = getPushshiftData(row[1], row[2])
    retrievedata(resultarray, row[3], row[4])