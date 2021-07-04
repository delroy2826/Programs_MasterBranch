#LINE GRAPH
#Example 1
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6] # X Co-ordinates
plt.xlabel("X-Axis") #Label For X Axis
y = [4,3,5,6,7,8]  # Y Co-ordinates
plt.ylabel("Y-Axis") # Label for Y Axis
plt.plot(x,y) #
plt.title("Title") #sets the title to the plot
plt.show() # displays the plot in a window

#Example 2
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6] # X Co-ordinates
plt.xlabel("X-Axis") #Label For X Axis
y = [4,3,5,6,7,8]  # Y Co-ordinates
x1 = [1,2,3,4,5,6]
y1 = [2,3,4,5,6,7]
plt.ylabel("Y-Axis") # Label for Y Axis
plt.plot(x1,y1,label='x1,y1',color='r')
plt.plot(x,y,label='x,y',color='k')
plt.title("Title") #sets the title to the plot
plt.legend()
plt.show() # displays the plot in a window

#Example 3
import matplotlib.pyplot as plt
x = [0,1,2,3,4,5,6,8]
plt.xlabel("X-Axis")
y = [3,4,3,5,6,7,8,1]
plt.xlim(0,9)
plt.ylim(0,9)
plt.ylabel("Y-Axis")
plt.plot(x,y,color='Green',linestyle='dashed',linewidth=2,marker='o',markerfacecolor='black',markersize=6)
plt.title("Title")
plt.show()

#example 4
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,1]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(0,5)
plt.ylim(0,5)
plt.plot(x,y,color = 'red',linestyle='dotted',marker='o',markerfacecolor='Blue',markersize=6)
plt.title('Line Plot Graph')
plt.show()

#Example 5
import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
x2 = [1,2,3]
y2 = [4,1,3]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x1,y1,label='Line 1',linestyle='dashed',color='blue',marker='o',markerfacecolor='black',markersize=5)
plt.plot(x2,y2,label='Line 2',linestyle='dotted',color='red',marker='o',markerfacecolor='yellow',markersize=5)
plt.title("Title")
plt.legend()
plt.show()

#Example 6
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
x1 = [1,2,3]
y1 = [2,4,1]
x2 = [1,2,3]
y2= [4,1,3]
plt.xlim(0,5)
plt.ylim(0,5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x1,y1,label='Line 1',linestyle='dashed',marker='o',markerfacecolor='orange',color='Blue',markersize=6.5,linewidth=3)
plt.plot(x2,y2,label='Line 2',linestyle='dashed',marker='o',markerfacecolor='green',color='red',markersize=6.5,linewidth=4)
plt.title('Title')
plt.legend()
plt.show()

#Example 7
import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
x2 = [1,2,3]
y2 = [4,1,3]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x1,y1,color='red',linestyle='dotted',linewidth=2.5,marker='o',markersize=2,label='Line 1')
plt.plot(x2,y2,color='blue',linestyle='dotted',linewidth=2.5,marker='o',markersize=2,label='Line 2')
plt.title('Line Graph')
plt.grid()
plt.legend()
plt.show()

#Example 8
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
Days = ['Day1','Day2','Day3','Day4']
plt.ylim(0,20)
Facts = [3,4,12,15]
plt.xlabel('Days')
plt.ylabel("Facts")
plt.plot(Days,Facts,linestyle='dotted',linewidth=2.5,marker='o',markerfacecolor='red',markersize=5.5,color='black')
plt.title('Facts I got Correct')
plt.show()

#Example 9
import numpy as np
import matplotlib.pyplot  as plt
Days = [1,2,3,4,5]
Enfield =[50,40,70,80,20]
Honda =[80,20,20,50,60]
Yahama=[70,20,60,40,60]
Ktm=[80,20,20,50,60]
plt.plot(Days,Enfield,label='Enfield',color = 'red',marker='o')
plt.plot(Days,Honda,label='Honda',color='Blue',marker='o')
plt.plot(Days,Yahama,label='Yahama',color='Green',marker='o')
plt.plot(Days,Ktm,label='Ktm',color='orange',marker='o')
plt.legend()
plt.show()


#Scatter Plot
#Example 1
x = [1,2,3,4,5,6]
plt.xlabel("X-axis")
y = [7,8,9,10,11,12]
plt.ylabel("Y-axis")
plt.scatter(x,y,label='Scatter Plot 1',color = 'red') #label is used to rep the color dots
plt.title("My Plot")
plt.legend() # Used to diplay the label of the color
plt.show()

#Example 2
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6] # X Co-ordinates
plt.xlabel("X-Axis") #Label For X Axis
y = [4,3.50,5,6,7,8]  # Y Co-ordinates
x1 = [1,2,3,4,5,6]
y1 = [2,3,4,5,6,7]
plt.ylabel("Y-Axis") # Label for Y Axis
plt.scatter(x1,y1,label='x1,y1',color='r')
plt.scatter(x,y,label='x,y',color='k')
plt.title("Title") #sets the title to the plot
plt.legend()
plt.show() # displays the plot in a window

Example 3
import matplotlib.pyplot as plt
x1 = [2,4,6,8,10,11,11.5,11.7]
y1= [1,1.5,2,2.5,3,3.5,4,4.5]
x2=[8,8.5,9,9.5,10,10.5,11]
y2=[3,3.5,3.7,4,4.5,5,5.2]
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.scatter(x1,y1,label='x1,y1',color='blue')
plt.scatter(x2,y2,label='x2,y2',color='red')
plt.legend()
plt.title('Scatter Plot')
plt.show()

#BAR GRAPH
#You can use bar graph
#when you have a categorical data and would like to represent the values proportionate to the bar lengths.
#Example 1
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')   #will change the background
x = ['2016','2017','2018']
y = [1252,1632,1692]
plt.xlabel("Year")
plt.ylabel("Number of Movies Released")
plt.bar(x,y,align='center',color='Blue')
plt.title('Bar Graph')
plt.show()

#Example 2
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')   #will change the background of the plot
movie_categories = ['Comedy','Action','Romance','Drama','SciFi']
rating = [4,5,6,1,4]
plt.title('Favorite Type of Movie')
plt.xlabel('movie_categories')
plt.ylabel('People Rating')
plt.bar(movie_categories,rating,color = 'Green')
plt.show()

#Example 3
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
Fruit = ['Apple','Orange','Banana','KiwiFruit','BlueBerry','Grapes']
Rating=[35,30,10,25,40,5]
plt.xlabel('Fruit')
plt.ylabel('People Rating')
plt.title('Nicest Fruit')
plt.bar(Fruit,Rating,color='Blue')
plt.show()

#Example 4
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
Grade =['A','B','C','D']
Students = [4,12,10,2]
plt.xlabel('Grades')
plt.ylabel('Students')
plt.title('Student Grades')
plt.bar(Grade,Students,color='Black')
plt.show()


















