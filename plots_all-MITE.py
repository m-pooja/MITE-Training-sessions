
"""
Created on Fri Dec  1 22:47:41 2017

@author: Pooja
www.poojaangurala.com
"""
"""
PLOTTING GRAPHS with MATPLOTLIB
this script presents :-
    Histogram
    scatter
    mtplotlib.gridspec
    pie chart
    bar chart
    parallel coordinates
    boxplots
    area plots
    
Try to run code lines seperately for better understanding of code.
use plt.clf() to clear the previous code.
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
x = np.linspace(0, 5, 10)
y = x ** 2
gdp_cap=[]
for i in range(50):
    n=np.random.randint(155, 389)
    n=n/100
    gdp_cap.append(n)
life_exp = []
for i in range(50):
    n=np.random.randint(100, 150)
    n=n/100
    life_exp.append(n)
pop = []
for i in range(50):
    n=np.random.randint(190, 230)
    n=n/100
    pop.append(n)
"""
histogram-----------------------------------
"""
plt.hist(pop, bins= 5)
plt.hist(pop, color='red')
plt.hist(pop, orientation='horizontal')# orientation changes the look of plot try it with 'vertical'
plt.xscale('log')
plt.yticks([0, 20000, 30000,50000])
pop=[31.889923, 3.6005229999999999, 33.333216, 12.420476000000001, 40.301926999999999, 20.434176000000001, 8.199783, 0.70857300000000001, 150.448339, 10.392226000000001, 8.0783140000000007, 9.1191519999999997, 4.5521979999999997, 1.6391309999999999, 190.01064700000001, 7.3228580000000001, 14.326203, 8.3905049999999992, 14.131857999999999, 17.696293000000001, 33.390141, 4.3690379999999998, 10.238807, 16.284741, 1318.683096, 44.227550000000001, 0.71096000000000004, 64.606758999999997, 3.8006099999999998, 4.1338840000000001, 18.013408999999999, 4.4933120000000004, 11.416987000000001, 10.228744000000001, 5.4681199999999999, 0.49637399999999998, 9.3196220000000007, 13.75568, 80.264543000000003, 6.9396880000000003, 0.55120100000000005, 4.9065849999999998, 76.511887000000002, 5.2384599999999999, 61.083916000000002, 1.4548669999999999, 1.6883589999999999, 82.400996000000006, 22.873338, 10.706289999999999, 12.572927999999999, 9.9478139999999993, 1.4720409999999999, 8.5028140000000008, 7.4837629999999997, 6.9804120000000003, 9.9561080000000004, 0.301931, 1110.3963309999999, 223.547, 69.453569999999999, 27.499638000000001, 4.1090859999999996, 6.426679, 58.147733000000002, 2.780132, 127.467972, 6.0531930000000003, 35.610177, 23.301725000000001, 49.044789999999999, 2.5055589999999999, 3.921278, 2.0126490000000001, 3.1939419999999998, 6.0369140000000003, 19.167653999999999, 13.327078999999999, 24.821286000000001, 12.031795000000001, 3.2700650000000002, 1.250882, 108.700891, 2.8741270000000001, 0.68473600000000001, 33.757174999999997, 19.951656, 47.761980000000001, 2.0550799999999998, 28.901789999999998, 16.570613000000002, 4.1157709999999996, 5.6753559999999998, 12.894864999999999, 135.03116399999999, 4.6279260000000004, 3.2048969999999999, 169.27061699999999, 3.2421730000000002, 6.6671469999999999, 28.674757, 91.077286999999998, 38.518241000000003, 10.642836000000001, 3.942491, 0.79809399999999997, 22.276056000000001, 8.8605879999999999, 0.19957900000000001, 27.601037999999999, 12.267493, 10.150264999999999, 6.1445619999999996, 4.5530090000000003, 5.4475020000000001, 2.0092449999999999, 9.1187729999999991, 43.997827999999998, 40.448191000000001, 20.378239000000001, 42.292929000000001, 1.1330659999999999, 9.0310880000000004, 7.5546610000000003, 19.314747000000001, 23.174294, 38.13964, 65.068149000000005, 5.7015789999999997, 1.056608, 10.276158000000001, 71.158647000000002, 29.170397999999999, 60.776237999999999, 301.13994700000001, 3.4474960000000001, 26.084662000000002, 85.262355999999997, 4.018332, 22.211742999999998, 11.746034999999999, 12.311143]
"""
Scatter ------------------------------------------------------
"""
import numpy as np
x= np.random.rand(5)
y=np.random.rand(5)
s1= [10,20,30,40,50]
c1=np.random.rand(5)
plt.scatter(x,y, s =s1, c=c1)

plt.scatter(gdp_cap, life_exp, s =pop)
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.legend(["curve1"])
fig, axes = plt.subplots(figsize=(12,3))
axes.xticks(0,2,4,6,8,10)
axes.yticks(0,2,4,6,8,10)
axes.plot(x, x**2, label="curve1")
axes.plot(x, x**3, label="curve2")
axes.legend()
#plt.clf()# clears the previous plt
fig, ax = plt.subplots()
ax.plot(x, x+1, color="red", alpha=0.5) # half-transparant red
ax.plot(x, x+2, color="#1155dd")        # RGB hex code for a bluish color
ax.plot(x, x+3, color="#15cc55")  
fig, axes = plt.subplots(1, 2, figsize=(10,3))

# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# customize grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

fig = plt.figure()
ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, t, color='blue', lw=3);

"""
gridspec---------------------------------------------------------
"""
import matplotlib.gridspec as gridspec
fig = plt.figure()

gs = gridspec.GridSpec(2, 3, height_ratios=[2,1], width_ratios=[1,2,1])
for g in gs:
    ax = fig.add_subplot(g)
    
fig.tight_layout()


"""
pie chart-----------------------------------------------------
"""

labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [310, 30, 145, 110]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # explode 1st slice
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.tight_layout()
plt.axis('equal')
plt.show()


"""
bar--------------------------------------------------------------
"""

x = np.arange(4)
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
a, b, c, d = plt.bar(x, money).scatter(True)
a.set_facecolor('r')
b.set_facecolor('g')
c.set_facecolor('b')
d.set_facecolor('black')
plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue'))
plt.show()

import pandas as pd

df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

df2.plot.bar();
df2.plot.bar(stacked=True);


"""
Parellel coordinates is a method for exploring the spread of multidimensional data 
on a categorical response, 
and taking a glance at whether there is any trends to the features.

Parallel coordinates is a plotting technique for plotting multivariate data. 
It allows one to see clusters in data and to estimate other statistics visually. 
Using parallel coordinates points are represented as connected line segments. 
Each vertical line represents one attribute. 
One set of connected line segments represents one data point. 
Points that tend to cluster will appear closer together.
"""
from pandas.tools.plotting import parallel_coordinates
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names) 
#print(dataset)
plt.figure()
parallel_coordinates(dataset , 'class')
print(dataset.groupby('class').size())

"""
box plot:
    The box plot (a.k.a. box and whisker diagram) is a standardized way of displaying the distribution of data based on the five number summary: minimum, 
    first quartile, median, third quartile, and maximum.
    In the simplest box plot the central rectangle spans the first quartile to the third quartile 
    (the interquartile range or IQR). A segment inside the rectangle shows the median and "whiskers" 
    above and below the box show the locations of the minimum and maximum.
If the data happens to be normally distributed,

IQR = 1.35 σ

where σ is the population standard deviation.
"""

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
df.plot.box(color=color, sym='r+')

"""
area plot:Area plots are stacked by default
    When input data contains NaN, it will be automatically filled by 0. If you want to drop or fill by different values, 
    use dataframe.dropna() or dataframe.fillna() before calling plot.
"""
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

df.plot.area();

"""
to be noted-------------------------

Pandas tries to be pragmatic about plotting DataFrames or Series that contain missing data. Missing values are dropped, left out, or filled depending on the plot type.

Plot Type	NaN Handling
Line	Leave gaps at NaNs
Line (stacked)	Fill 0’s
Bar	Fill 0’s
Scatter	Drop NaNs
Histogram	Drop NaNs (column-wise)
Box	Drop NaNs (column-wise)
Area	Fill 0’s
Pie	Fill 0’s
"""