import csv
from psaw import PushshiftAPI

api = PushshiftAPI()

with open('postsbyday.csv','w',newline="", encoding="utf-8") as filewriter:
    writer=csv.writer(filewriter)

    with open('alldates.csv', 'r') as filereader:
        reader = csv.reader(filereader)

        for row in reader:
            gen = api.search_submissions(after=row[1],
                                         before=row[2],
                                         subreddit='soccer',
                                         limit=2500)

            results = list(gen)

            print(row[0])
            writer.writerow([row[0],len(results)])