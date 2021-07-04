import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1,y1,label='Line 1',linewidth=5,color = 'red')
x = [1,2,3]
y = [4,1,3]
plt.plot(x,y,label='Line 2',linewidth=5,color = 'blue')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('Two Lines on same Graph')
plt.legend()
plt.grid(True,color='green')
plt.show()

from matplotlib import pyplot as plt
x1 = [0.25,1.25,2.25,3.25,4.25]
y1 = [50,40,70,80,20]
x2 = [0.75,1.75,2.75,3.75,4.75]
y2 = [80,20,20,50,60]
plt.bar(x1,y1,label='BMW',width=0.5,color = 'red')
plt.bar(x2,y2,label='Audi',width=0.5,color = 'blue')
plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance in Km")
plt.title('Information')
#plt.grid(color='green',width = 10)
plt.show()

import matplotlib.pyplot as plt
pop_age=[21,22,23,23,25,12,23,45,56,34,56,67,34,23,54,34,23,34]
bins=5
plt.hist(pop_age,bins,histtype='bar',color='blue',rwidth=0.5)
plt.xlabel('Age Groups')
plt.ylabel('Number of People')
plt.title('Histogram Graph')
plt.show()

import matplotlib.pyplot as plt
x1 = [1,2,3,4,5,6,7,8,9]
y1 = [7,5,5,6,3,7,2,8,1]

x2 = [11,22,33,22,33,44,55,22,33]
y2 = [33,44,22,33,33,11,22,33,44]
plt.scatter(x1,y1,label='High income saving',color='r')
plt.scatter(x2,y2,label='Low Income Savings',color='b')
plt.xlabel('x-asixs')
plt.ylabel('Y-axis')
plt.title('scatter plotting graph')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
plt.plot(year, pop_pakistan, color='g')
plt.plot(year, pop_india, color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x,y,color='green',linewidth=5, linestyle='dotted')
plt.show()