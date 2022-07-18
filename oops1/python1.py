"""
Python Keyword are the reserved words in Python.
We canot use a keyword as a variable name, function name or any
other identifiers. They are used to define the syntax and structure of
 the python languages.
 In python, Keyword are case sensitive.
 There are 33 reserved keywords in python 

 Python Identifiers:
 An identifier is a name given to entities like class, functions
 variables, etc. it help to differentiate one entity from another.

Variables is a named location used to store data in the memory.
It is helpful to think of variables as a container that hold data
that can be changed later in the program

Literals
Literals is a raw data given in a variables or constant. In python
, there are various types of literals they are as follows:

Numerical literals : Numerical literals are immutable(unclangeable).
it belongs to 3 different types Integerm Float, Complex.

Strings literals :  A strings literals are a sequence of character
sorrounded by quotes. we can user both single or double or triple quotes.

Python List : List is an ordered sequence of items. It is one of the 
most used datatypes in python and is flexible. All the items in a list do not need to be of
sane types.

Python Tuples : Tuples is a orderd sequence of items same as a list.
The only difference is that tuples are immutables. Tuples once created cannot
be changed.

Python strings : Python strings is a sequence of Unicode characters. We use single or doubles quotes to
represent strings.strings are immutables.

Python set : Set is an unordered collection of unique items.Set is defined by values 
seperated by comma inside braces {}. Items in a set are not ordered.
we can perform set operations like union, interaction on two set. set have unique values
They eliminate duplicates.

Python Dictionary :  Python dictionary is an unorderd collections of Key-values pairs.
It generally used when we have huge amout of data.


"""

# String slicing
# name =  "Python"
# print(name[-1::-1])
# name = input("Enter your name : ")
# reverse = name[-1::-1]
# print(f"Your reverse name is {reverse}.")
# print(len(name))

# Escape sequence
# print("Line A \nLine B")

# Space problem using strip
# name = input("Enter your name :")
# name = name.strip()
# print(name)
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.count('i'))
# name = name.rstrip()
# name = len(name)

# print(name)


# lang = 'English'
# lang.replace("E", "T")
# print(lang)

# new_lang = lang.replace("E", "@")
# print(new_lang)

# age = int(input("Enter your age :"))
# print(age)
# print(type(age))
# if age > 18:
#     print("You can play.")
# else:
#     print("You cant play.")


# wn = 99
# ui = int(input("Guess a number between 90 - 100 : "))    
# if ui==wn:
#     print("YOU WON.")
# else:
#     if ui < wn:
#         print("Too low.")
#     else:
#         print("Too high.")

# # ticket fee app
# age = int(input("Enter your age : "))
# if age <=0:
#     print("You are not eligiable for ticket.")
# elif 1<= age <=5:
#     print("Your ticket price is free.")
# elif 6<=age<=10:
#     print("Your ticket price is Rs. 150.")
# elif 11<=age<=60:
#     print("Your ticket price is Rs. 250.")
# elif 60<age<=100:
#     print("your ticcket price is Rs. 200")

# While loop/for loop/
# i = 1
# while i<=10:
#     print(f"My name is Dillip Singh. ----{i}")
#     i+=1

# # Write a program to sum 1--10
# total = 0
# i = 1
# while i<=10:
#     total += i
#     i+=1
# print(total)

# # Write a program to sum the natural number you enter
# number = int(input("Enter the Natural number : "))
# total = 0
# i = 1
# while i<=number:
#     total += i
#     i+=1
# print(total)

# # Write a sequence of number and sum all digit
# number = input("Enter the sequence of number : ")
# total = 0
# i = 0
# # print(number[0])
# # print(len(number))
# while i < len(number):
#     total += int(number[i])
#     i+=1
# print(total)

# # Write a program to count character in your name
# name = input("Enter your name : ")
# temp = ""
# i=0
# while i < len(name):
#     if name[i] not in temp:
#         temp +=name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i+=1

# # for loop
# for i in range(1,11):
#     print(f"Dillip---{i}")

# # Fibonacci series program

# def fibonacci_series(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a,b)
#     else:
#         print(a,b, end=" ")
#     for i in range(n-2):
#         c = a+b
#         a=b
#         b=c
#     print(b, end=" ")
# fibonacci_series(2)

# # Is_Palindrome
# name = input("Enter the number : ")
# reverse = name[-1::-1]
# # print(reverse)
# if name == reverse:
#     print("Palindrome")
# else:
#     print("Not_Palindrome")

# # Greatest_Number
# def greatest_number(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# # print(greatest_number(3,2,4))

# a,b,c = input("Enter three comma seperated number:").split(",")
# a = int(a)
# b = int(b)
# c = int(c)
# print(greatest_number(a,b,c))

# # local and global variable
# x = 5
# def fun1():
#     x = 5
#     print(x)
# # print(fun1())
# fun1()

# # break and continue
# for i in range(10):
#     if i==5:
#         break
#     print(i)
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i, end=" ")

# # loop inside string
# for i in "dillip":
#     print(i, end=" ")

# # step arguement in range funstions:
# for i in range(1,11,2):
#     print(i, end=" ")

# # Do sum using for loop
# number = input("Enter the number : ")
# total = 0
# for i in range(0, len(number)):
#     total += int(number[i])
# print(total)

# number = int(input("Enter the number : "))
# total = 0
# for i in range(1, number+1):
#     total += i
# print(total)


# Dry principal(dont repeat yourself)
# # number gussing game
# wn = 50
# un = int(input("Enter the number : "))
# guess = 1
# go=False
# while not go:
#     if un==wn:
#         print(f"You Won the game in {guess} time.")
#         go = True
#     else:
#         if un<wn:
#             print("too low.")
#             # guess +=1
#             # un = int(input("Enter the number again : "))
#         else:
#             print("too high")
#             # guess +=1
#             # un = int(input("Enter the number again : "))
    
#     guess += 1 
#     un = int(input("Enter the number again : "))