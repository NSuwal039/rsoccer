import pandas as pd
import matplotlib.pyplot as plt

filename = 'postsbyday.csv'
df = pd.read_csv(filename)

xmas = df[df['Date'].str.contains('/25/')]

x = xmas['Date']
y= xmas['Posts']

plt.title('Number of posts on Christmas')
plt.xlabel('Date')
plt.ylabel('Posts')
plt.plot(x,y)

plt.show()