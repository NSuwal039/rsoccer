import pandas as pd
import csv
import matplotlib.pyplot as plt

filename = 'subscribers_growth.csv'
df = pd.read_csv(filename)

df = df.drop(df[df['y'].str.contains("2012|2020")].index)
# print(remove)

df = df[['y', 'a']]
# print(remove1)

dates = ["-12-18",
         "-12-19",
         "-12-20",
         "-12-21",
         "-12-22",
         "-12-23",
         "-12-24",
         "-12-25",
         "-12-26",
         "-12-27",
         "-12-28",
         "-12-29",
         "-12-30",
         "-12-31",
         "-01-01"]

pattern = '|'.join(dates)

print(pattern)

df = df[df.y.str.contains(pattern)]

final = df.drop(df[df['y'].str.contains("2019-12|2013-01")].index)

final.to_csv("filtered_subscribers_growth.csv")