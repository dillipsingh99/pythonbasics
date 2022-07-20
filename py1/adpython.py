"""
*args and **kwargs in Python :
The special syntax *args in function definition in python is used to pass a
variable number of argument to a function. It is used to pass a non-key worded 
variable length argument list.
"""

# def myfun(*args):
#     for arg in args:
#         print(arg)

# myfun('Hello', 'welcome', 'to', 'GeeksforGeeks')

# def myfun(arg1, *args):
#     print(f"My first argument : {arg1}")
#     for arg in args:
#         print(f"My next arguement is :", arg)
# myfun('Hello', 'welcome', 'to', 'GeeksForGeek')

"""
What is python **kwargs ?
The special syntax **kwargs in function definition in python is used to pass a 
keyword, variable-length arguement list.
"""
# def myfun(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}=={value}")

# myfun(first='geeks', mid='for', last='Geeks')

# def myfun(arg1, **kwargs):
#     print(f"single value arguement {arg1}")
#     for key,value in kwargs.items():
#         print(f"{key}=={value}")

# myfun("dj", first="dillip", mid="kumar", last='singh')

# def myFun(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
 
 
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

"""
Generator-function: A generator function is define like a normal function but
when ever it needs to generate a value, it does so with the yield keyword rather then return.
if the body of a def contains yields the functions automatically becomes a generator function.
"""
# def simplegeneratorfun():
#     yield 1
#     yield 2
#     yield 3

# for value in simplegeneratorfun():
#     print(value)

"""
Generator objects: Generator function return a generator objects.
Generator objects are used either by calling the next method on the
generator objects or using the generator objects in a "for loop".
"""
# def simplefunction():
#     yield 1
#     yield 2
#     yield 3

# x=simplefunction()

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# Generator for fibonacci Number
# def fib(n):
#     a,b = 0,1
#     while a < n:
#         yield a
#         a,b = b, a+b
# x = fib(5)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# for i in fib(10):
#     print(i, end=" ")

"""
PYTHON CLOSURES
Nasted functions in Python:
A function that is defined inside another function is Known as 
Nasted function.
"""
# def outerfunction(text):
#     text = text

#     def innerfunction():
#         print(text)
#     innerfunction()

# if __name__=='__main__':
#     outerfunction('Hey')

# def outerfun(text):
#     def innerfun():
#         print(text)
#     innerfun()
# outerfun('Hello  ')

# def pop(list):
#     def get_last_item(my_list):
#         return my_list[len(list)-1]
#     list.remove(get_last_item(list))
#     return list

# a = [1,2,3,4,5,6]
# print(pop(a))
# print(pop(a))
# print(pop(a))
# print(pop(a))

"""
Python Closure :
A Closure is a function object that remembers valueus in enclosing
scopes even if they are not present in memory.
"""
# def outerfun(text):
#     def innerfun():
#         print(text)
#     return innerfun
# a = outerfun("Hello")
# a()

# def nth_power(expo):
#     def square(base):
#         return pow(base, expo)
#     return square
# a = nth_power(2)
# print(a(2))
# print(a(3))
# print(a(4))

"""
Decorators in Python:
Python has an interesting feature called decorators to add functionallity to an
existing function.
This is also called metaprogramming because a part of the program tries to modify
another part of the progeam at compile time.
"""
# def inc(x):
#     return x+1
# def dec(x):
#     return x-1
# def operate(fun, x):
#     result = fun(x)
#     return result

# # A function that takes other function as an arguments are also called higher
# # order function
# print(operate(inc, 3))
# print(operate(dec, 4))

# def is_called():
#     def is_returned():
#         print("Hello")
#     return is_returned
# new = is_called()
# new()

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#         print("Just ignore.")
#     return inner
# def ordinary():
#     print("I am ordinary")

# doc = make_pretty(ordinary)
# doc()

# def smart_divide(fun):
#     def inner(a,b):
#         print(f"I am going ot divide {a} and {b}")
#         if b == 0:
#             print("whoops! cannot divide.")
#             return
#         return fun(a,b)
#     return inner
# # @smart_divide
# def divide(a,b):
#     print(a/b)

# divide(2,0)

# def star(fun):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         fun(*args, **kwargs)
#         print("*"*30)
#     return inner

# def percent(fun):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         fun(*args, **kwargs)
#         print("%" * 30)
#     return inner

# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("Hello")