"""
Python classes/Objects
Python is an objects oriented programming language.
All most everythings in python is an objects, with its properties and methods.
A class is like an object constructor or a "blueprint for creating objects.
"""

# class MyClass():
#     x = 5

# p1 = MyClass()
# print(p1.x)

"""
The __init__() function:
To understand the meaning of class we have to understand the meaning of built_in __init__() function.
All classes have built in __init__() which is always executed when the class is being initiated.

"""
# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Dillip", 27)
# print(p1.name)
# print(p1.age)

# NOTE: The __init__() function is called automatically every time the class is being
# used to create a new objects.

"""
Objects can also contain method. Methods in objects are functions that belongs 
to the objects.
"""

# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

#     def myfunction(self):
#         print(f"Hello my name is " + self.name)


# p1 = Person("Dillip", 27)
# p1.myfunction()

"""
Python Inheritance : Inheritance allows us to define a classes
that inherit all the methods and properites from another class.
Parent class is base class.
child class inherit from another class.
"""

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(f"{self.firstname} {self.lastname}")

#     def fullname(self):
#         print(f"My full name is {self.firstname} {self.lastname}")

# class Student(Person):
#     def __init__(self, firstname, lastname, comp):
#         # Person.__init__(self, fname, lname)
#         super().__init__(firstname, lastname)
#         self.comp = comp

#     def first_name(self):
#         print(f"My first name is {self.firstname}")

#     def graduation(self):
#         print(f"I have completed my graduation in {self.comp}")

#     def detail(self):
#         print(f"My name is {self.firstname} {self.lastname}. I have completed my graduation in {self.comp}.")

# p1 = Student("Dillip", "Singh", 2021)
# # p1.comp = 2022

# p1.printname()
# p1.first_name()
# p1.graduation()
# p1.fullname()
# p1.detail()


"""
Python Iterators : An iterator is an objects that contains a countable number of values.
it consist __iter__() and __next__() metods.
List, tuples, dictionary, set are all iterables objects. They are iterable containers which  you canm
 get an iterator from.
All these objects have a iter() method which is uesd to get an iterator.

"""
# mytuple = ("apple", "banana" , "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))

"""
Create an iterator
"""
# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x

# myclass = MyNumber()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a +=1
            return x
        else:
            raise StopIteration    
myclass = MyNumber()
myiter = iter(myclass)

for i in myiter:
    print(i, end=" ")