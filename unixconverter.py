from datetime import datetime, date
import calendar
import csv

utcdates = [[2018, 12, 18],
            [2018, 12, 19],
            [2018, 12, 20],
            [2018, 12, 21],
            [2018, 12, 22],
            [2018, 12, 23],
            [2018, 12, 24],
            [2018, 12, 25],
            [2018, 12, 26],
            [2018, 12, 27],
            [2018, 12, 28],
            [2018, 12, 29],
            [2018, 12, 30],
            [2018, 12, 31],
            [2018+1, 1, 1],
            ]

for i in utcdates:
    print(i[0],i[1],i[2])

with open('2018dates.csv','w',newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['datetime','from','to','filename','mode'])

    c=0
    mode='w'
    for i in utcdates:
        d1 = datetime(i[0], i[1], i[2], 0, 0, 0)
        d2 = datetime(i[0], i[1], i[2], 23, 59, 59)
        timestamp1 = calendar.timegm(d1.timetuple())
        timestamp2 = calendar.timegm(d2.timetuple())
        if c==0 or c==7 or c==8:
            mode='w'
        else:
            mode='a'

        if 0<=c<7:
            filename='beforexmas2018'
        elif c==7:
            filename='xmas2018'
        else:
            filename='afterxmas2018'

        writer.writerow([str(i[0])+"/"+str(i[1])+"/"+str(i[2]),timestamp1,timestamp2,filename,mode])
        c+=1
