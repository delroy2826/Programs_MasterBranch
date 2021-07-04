#1
def outer_function():
    message = "Hi"
    def inner_function():
        print(message)
    return inner_function()
outer_function()

#2
def outer_function():
    message = "Hi"
    def inner_function():
        print(message)
    return inner_function
my_func = outer_function()
print(my_func)

#3
def outer_function():
    message = "Hi"
    def inner_function():
        print(message)
    return inner_function
my_func = outer_function()
print(my_func.__name__)

#4
def outer_function():
    message = "Hi"
    def inner_function():
        print(message)
    return inner_function
my_func = outer_function()
print(my_func.__name__)
my_func()

#5
def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function
my_func1 = outer_function("Hi")
my_func2 = outer_function("Hello")
my_func1()
my_func2()

#6
def outer_function():
    message = input("Enter the Message:")
    def inner_function():
        print(message)
    return inner_function
my_func1 = outer_function()
my_func2 = outer_function()
my_func2()
my_func1()

#7
def outer_function():
    message = input("Enter the Message:")
    def inner_function():
        print(message)
    return inner_function
my_func1 = outer_function()
my_func2 = outer_function()
del outer_function
my_func2()
my_func1()

#8
def outer_funtion(a):
    def inner_function(n):
        return a + n
    return inner_function
f = outer_funtion(10)
print(f(2))
print(f.__name__)