from psaw import PushshiftAPI
import datetime as dt
import csv

api = PushshiftAPI()

gen = api.search_submissions(after=1513630000,
                             filter=['id','title', 'author', 'score', 'domain', 'url', 'num_comments', 'created_utc',
                                     'selftext'],
                             subreddit='soccer',
                             before=1513650000,
                             limit=250)
results = list(gen)
print(type(results))

# print("selftext" in results[0].d_,)
# print(results[0].d_['id'])
# print(results[0].d_['title'])
# print(results[0].d_['author'])
#
# print(results[0].d_)
# results[0].d_['selftext']="empty"
# print(results[0].d_)

c=0
for i in results:
    if "selftext" in i.d_:
        c+=1

print(c)