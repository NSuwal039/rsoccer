from psaw import PushshiftAPI
import datetime as dt
import csv

api = PushshiftAPI()


def getRedditData(from_epoch, to_epoch):
    gen = api.search_submissions(after=from_epoch,
                                 limit=5000,
                                 filter=['title', 'author', 'score', 'domain', 'url', 'num_comments', 'created_utc',
                                         'selftext'],
                                 subreddit='soccer',
                                 before=to_epoch
                                 )
    results = list(gen)

    for i in results:   
        if "selftext" not in i.d_:
            i.d_["selftext"]=""

    return results


def writeRedditData(redditData, filename, modec):
    with open(filename + '.csv', modec, newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if modec == 'w':
            writer.writerow(['title', 'author', 'score', 'domain', 'url', 'num_comments', 'created_utc', 'selftext'])

        for i in redditData:
            writer.writerow([i.d_['title'],
                            i.d_['author'],
                            i.d_['score'],
                            i.d_['domain'],
                            i.d_['url'],
                            i.d_['num_comments'],
                            i.d_['created_utc'],
                            i.d_['selftext']])


filereader = open('2015dates.csv', 'r')
csvreader = csv.reader(filereader)

col_num = next(csvreader)

for row in csvreader:
    print(row)
    redditArray = getRedditData(row[1], row[2])
    writeRedditData(redditArray, row[3], row[4])
