#Importing Numpy module and setting the reference as np
import numpy as np

#1
#Creating numpy array using Python list (One-Dimensional Array)
l=[1,2,3,4,5,6]
my_numpy_list=np.array(l)
print(my_numpy_list) #One Dimensional Array

#2
#Creating Two-Dimensional numpy Array using python nested list
l2 = [[1,2,3],[4,5,6],[7,8,9]]
my_2d_numpy_list = np.array(l2)
print(my_2d_numpy_list) #Two-Dimensional Array

#3
#Creating Numpy array using arange() built-in funtion
my_list=np.arange(11)
print(my_list)

#arange(start,stop,step)
my_list=np.arange(2,11,2)
print(my_list)

#4
#We can also generate an One-Dimensional array of 5 zeros
#Ex1
my_list=np.zeros(5) #columns
print(my_list)

#Ex2
array = np.zeros((4,4)) #rows and columns
print(array)

#Ex3
array = np.zeros((4,4,3)) # 4 Number of arrays of zeros with 4 rows and 3 columns
print(array)

#We can also generate an One-Dimensional array of 5 ones
#Ex1
my_list=np.ones(5)
print(my_list)

#Ex2
array = np.ones((2,4,5)) #2 Number of arrays with 4 rows and 5 columns
print(array)


#5
#we could generate a two-dimensional array of zeros having 3 rows and 5 columns
my_list = np.zeros((3,5))
print(my_list)

#we could generate a two-dimensional array of ones having 3 rows and 5 columns
my_list = np.ones((3,5))
print(my_list)

#6
#Creating NumPy array using linspace() built-in function.
#The linspace() function returns numbers evenly spaced over a specified intervals
# linspace() takes the third argument as the number of datapoints to be created.
my_list = np.linspace(1,3,5)
print(my_list) #one dimensional vector.

#7
#Creating an identity matrix in NumPy
#he number of row is equal to the number of column.
#One unique thing to note about identity matrix is that the diagonals are 1’s and everything else is 0.
#Identity matrices usually takes a single argument.
#Ex1
np_array = np.eye(6) #6 is the number of columns/rows you want
print(np_array)

#Ex2
array = np.eye(5,4) #5 rows and 4 columns
print(array)

#8
#Generating an array of random numbers in NumPy
#Using random.rand()
#we can generate an array of random numbers of the shape we pass to it from uniform
#distribution over 0 to 1.
#random.rand(number of arrays,rows, columns)
#ex1
my_rand = np.random.rand(3) #columns
print(my_rand)

#ex2
my_rand = np.random.rand(3,3) #rows and columns
print(my_rand)

#ex3
my_rand = np.random.rand(2,3,3) #number of arrays,rows, columns
print(my_rand)

#Using random.randn()
#we can generate random samples from Standard, normal or Gaussian distribution centered around 0.
#random.randn(number of arrays,row,columns)
#ex1
my_randn = np.random.randn(4) #columns
print(my_randn)

#ex2
my_randn = np.random.randn(2,4) #rows and columns
print(my_randn)

#ex3
my_randn = np.random.randn(2,2,4) #number of arrays,row,columns
print(my_randn)

#Using random.randint()
#we can use the randint() function to generate an array of integers.
#The randint() function can take up to 3 arguments;
#the low(inclusive), high(exclusive) and size of the array.
#random.randint(low(inclusive),high(exclusive),size of array)

#ex1
my_randint = np.random.randint(25) #np.random.randint(20) #generates a random integer exclusive of 25
print(my_randint)

#ex2
my_randint = np.random.randint(5,20) #generates a random integer including 5 but excluding 20
print(my_randint)

#ex3
my_randint = np.random.randint(5,20,7) #generates 7 random integers including 5 but excluding 20
print(my_randint)


#9
#Converting one-dimensional array to two-dimensional
#The reshape() can only convert to equal number or rows and columns
#and must together be equal to equal to the number of elements

#ex1
arr = np.random.rand(16)
print(arr.reshape(4,4))

#ex2
my_array = np.arange(16)
print(my_array)
print(my_array.reshape(4,4))

#ex3
l = [1,2,3,4,5,6]
array = np.array(l).reshape(3,2)
print(array)

#ex4
array = np.arange(25).reshape(5,5)
print(array)

#ex5
array = np.random.randint(0,25,25).reshape(5,5)
print(array)

#10
#Locating the maximum and minimum values of a NumPy Array
#Using the max(), and min(), we can get the maximum or minimum values in an array.
#Ex1
l = [1,2,3,4,5,6]
my_array=np.array(l)
print(np.max(my_array))
print(np.min(my_array))

#ex2
my_array = np.random.randint(1,20,10)
print(np.max(my_array))
print(np.min(my_array))

#ex3
my_array = np.arange(1,20)
print(np.min(my_array))
print(np.max(my_array))


#Using the argmax() and argmin() functions, we can locate the index of the maximum or minimum values in an array.
#Ex4
my_array = np.arange(1,20)
print(my_array)
print(np.argmin(my_array))
print(np.argmax(my_array))

#Ex5
my_array = np.random.randint(1,20,10)
print(my_array)
print(np.max(my_array))
print(np.min(my_array))
print(np.argmax(my_array))
print(np.argmin(my_array))

#Ex6
l = [1,2,3,4,5,6]
my_array=np.array(l)
print(np.argmax(my_array))
print(np.argmin(my_array))

#ex7
l = [1,2,3,4,5,6]
array = np.array(l).max()
print(array)
array = np.array(l).min()
print(array)
array = np.array(l).argmax()
print(array)
array = np.array(l).argmin()
print(array)
array = np.random.randint(0,25,5).argmax()
print(array)

#11
#To check whether the array is one dimensional or two dimensional
#1
l = [[1,2],[3,4],[5,6]]
my_array=np.array(l)
print(np.shape(my_array))

#2
l = [1,2,3,4,5,6]
my_array=np.array(l)
print(np.shape(my_array))

#12
#Indexing/Selecting elements or groups of elements from a NumPy array
#Ex1
l = np.arange(1,20,2)
print(l) #[ 1  3  5  7  9 11 13 15 17 19]
print(l[2:4]) #This returns everything from index 2 to 4(exclusive)
print(l[:8]) #This returns everything from index 0 to 8(exclusive)
print(l[2:]) #This returns everything from index 2 to the end of the array.

#Ex2
l = [[11,22,33],[44,55,66],[77,88,99]]
my_array=np.array(l)
print(my_array[1,2])
print(my_array[0,2])
print(my_array[2,1])
print(my_array[1:])
print(my_array[1,1:2])
print(my_array[:,:2])
print(my_array[:2,:2])

#13
#We can also perform conditional and logical selections
#on arrays using & (AND), | (OR), <, > and == operators to
#compare the values in the array with the given value.

#ex1
l = [1,2,3,4,5,6,7,8,9,10]
my_array=np.array(l)
print(my_array >= 5)

#ex2
l = [1,2,3,4,5,6,7,8,9,10]
my_array=np.array(l)
a=my_array >5
print(my_array[a])

#ex3
l = [1,2,3,4,5,6,7,8,9,10]
my_array=np.array(l)
a=my_array >5
print(my_array[(my_array >3) & (my_array<7)])

#14
#Broadcasting
#Broadcasting is a quick way to change the values of a NumPy array.
#
l = [1,2,3,4,5,6,7,8,9,10]
my_array=np.array(l)
my_array[:5] = 0
print(my_array)

#15
#Performing arithmetic operations on NumPy Arrays
#Ex1
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,22,33,44,55,66,77,88,99,100]
array1=np.array(list1)
array2=np.array(list2)
print(array1*array1) #Multiplies each element by itself
print(array1*array2)
print(array1-array1) #Subtractes each element by itself
print(array1-array2)
print(array1+array1) #Adds each element by itself
print(array1+array2)
print(array1/array1) #Divides each element by itself
print(array1/array2)

#We can also perform scalar operations on an array. NumPy makes it possible through broadcasting.
#Ex1

list1 = [1,2,3,4,5,6,7,8,9,10]
array1=np.array(list1)
print(array1*2) #This adds 50 to every element in that array
print(array1+2)
print(array1-2)
print(array1/2)

#Numpy also let’s you perform universal functions such as square roots, exponentials, trigonometric, etc on array.

#Ex1
list1 = [1,2,3,4,5,6,7,8,9,10]
array1=np.array(list1)
print(np.sqrt(array1)) #Returns the square root of each element
print(np.sum(array1)) #Returns the sum total of elements in the array
print(np.std(array1)) #Returns the standard deviation of in the array
print(np.exp(array1)) #Returns the exponentials of each element
print(np.log(array1)) #Returns the logarithm of each element

#Ex2
mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat.sum())         #Returns the sum of all the values in mat
print(mat.sum(axis=0))   #Returns the sum of all the columns in mat
print(mat.sum(axis=1))   #Returns the sum of all the rows in mat