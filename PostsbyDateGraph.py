import pandas as pd
import matplotlib.pyplot as plt

filename = 'postsbyday.csv'
df = pd.read_csv(filename)

def plotbyyear(year):
    filtered = df[df['Group'] == year]
    dates = filtered['Date']

    dates_final = []
    for e in dates:
        dates_final.append(str(e)[0:5])

    data = {'Date': dates_final,
            'Posts': filtered['Posts']}

    finaldata = pd.DataFrame(data, columns=['Date', 'Posts'])

    x_axis = finaldata['Date']
    y_axis = finaldata['Posts']

    plt.title('Number of posts by day ' + str(year))
    plt.xlabel('Date')
    plt.ylabel('Posts')
    plt.plot(x_axis, y_axis)
    #plt.savefig(str(year)+'.png')
    plt.show()

plotbyyear(2018)