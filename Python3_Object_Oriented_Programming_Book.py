# - Chapter 1 Object-oriented Design

# UML - (Unified Modeling Language)


# - Chapter 2 Objects in Python



# simple class definition
# class MyFirstClass:
#     pass



# adding attributes
# class Point:
#     pass
# p1 = Point()
# p2 = Point()

# p1.x = 5
# p1.y = 4

# p2.x = 3
# p2.y = 6

# print(p1.x, p1.y)
# print(p2.x, p2.y)



# adding methods
# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0
# p = Point()
# p.x = 5
# p.y = 4
# print(p.x, p.y)
# p.reset()
# print(p.x, p.y)



#
# import math
# class Point:
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#     def reset(self):
#         self.move(0, 0)
#     def calculate_distance(self, other_point):
#         return math.sqrt(
#         (self.x - other_point.x)**2 +
#         (self.y - other_point.y)**2)
# # how to use it:
# point1 = Point()
# point2 = Point()
# point1.reset()
# point2.move(5,0)
# print(point2.calculate_distance(point1))
# assert (point2.calculate_distance(point1) ==
#     point1.calculate_distance(point2))
# point1.move(3,4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))



# full point class definition
# import math
# class Point:
#     'Represents a point in two-dimensional geometric coordinates'
#     def __init__(self, x=0, y=0):
#         '''Initialize the position of a new point. The x and y
#         coordinates can be specified. If they are not, the point
#         defaults to the origin.'''
#         self.move(x, y)
#     def move(self, x, y):
#         "Move the point to a new location in two-dimensional space."
#         self.x = x
#         self.y = y

#     def reset(self):
#         'Reset the point back to the geometric origin: 0, 0'
#         self.move(0, 0)
#     def calculate_distance(self, other_point):
#         """Calculate the distance from this point to a second point
#         passed as a parameter.
#         This function uses the Pythagorean Theorem to calculate
#         the distance between the two points. The distance is returned
#         as a float."""
#         return math.sqrt(
#             (self.x - other_point.x)**2 +
#             (self.y - other_point.y)**2)


# models
# import database
# db = database.Database()
# # Do queries on db

# from database import Database
# db = Database()
# # Do queries on db

# from database import Database as DB
# db = DB()
# # Do queries on db



# parent_directory/
#     main.py
#     ecommerce/
#         __init__.py
#         database.py
#         products.py
#         payments/
#             __init__.py
#             paypal.py
#             authorizenet.py


# absalute import
# import ecommerce.products
# product = ecommerce.products.Product()
# or
# from ecommerce.products import Product
# product = Product()
# or
# from ecommerce import products
# product = products.Product()


#relative import
# from .database import Database
# from ..database import Database
# from ..contact.email import send_mail


# class SecretString:
#     '''A not-at-all secure way to store a secret string.'''
#     def __init__(self, plain_string, pass_phrase):
#         self.__plain_string = plain_string
#         self.__pass_phrase = pass_phrase

#     def decrypt(self, pass_phrase):
#         '''Only show the string if the pass_phrase is correct.'''
#         if pass_phrase == self.__pass_phrase:
#             return self.__plain_string
#         else:
#             return ''
        
# secret_string = SecretString("ACME: Top Secret", "antwerp")
# print(secret_string.decrypt("antwerp"))
# print(secret_string.__plain_string)


"""
Exercises
Write some object-oriented code. The goal is to use the principles and syntax you
learned in this chapter to ensure you can use it, instead of just reading about it. If
you've been working on a Python project, go back over it and see if there are some
objects you can create and add properties or methods to. If it's large, try dividing it
into a few modules or even packages and play with the syntax.
If you don't have such a project, try starting a new one. It doesn't have to be
something you intend to finish, just stub out some basic design parts. You don't
need to fully implement everything, often just a print("this method will do
something") is all you need to get the overall design in place. This is called
top-down design, when you work out the different interactions and describe
how they should work before actually implementing what they do. The converse,
bottom-up design, implements details first and then ties them all together. Both
patterns are useful at different times, but for understanding object-oriented
principles, a top-down workflow is more suitable.
If you're having trouble coming up with ideas, try writing a TO DO application.
(Hint: It would be similar to the design of the notebook application, but with extra
date management methods.) It can keep track of things you want to do each day, and
allow you to mark them as completed.
Now, try designing a bigger project; it doesn't have to actually do anything, but
make sure you experiment with the package and module importing syntax. Add
some functions in various modules and try importing them from other modules and
packages. Use relative and absolute imports. See the difference, and try to imagine
scenarios where you would want to use each one.
"""



# Chapter 3 When Objects are Alike -\|/-

# class Contact:
#     all_contacts = []

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)


# Chapter 4
# Chapter 5
# Chapter 6
# Chapter 7
# Chapter 8
# Chapter 9
# Chapter 10
# Chapter 11
# Chapter 12