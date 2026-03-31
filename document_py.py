# # -*- coding: utf-8 -*-

# print("A\nb\tc")

# print(r"A\nb\tc")

# print('pyth' 'on')

# print('Put several strings within parentheses '
#         'to have them joined together.')

# print("Python"[0])

# print("Python"[-1])

# print("python"[0]+"python"[-1])

# #  wrong formula print("python"[0]="o")

# print(len("Pythom"))

# print('Python'.center(10, '='))

# print('Python'.count("Python",1,3))

# print('01\t012\t0123\t01234'.expandtabs(8))

# print('Python'.find('h',0,5))

# print("The sum of 1 + 2 is {0}".format(1+2))

# print("The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2))

# print('-'.join("python"))


# print('python'.ljust(10,'.'))

# print('a b c'.split())


# print('www.example.com'.lstrip('cmowz.'))

# print('Arthur: three!'.removeprefix('Arthur: '))

# print("Monty Python's Flying Circus".partition(' '))

# print('Python'.encode())

# print('Python'.endswith('h',0,4))


# Lists

# squares = [1, 4, 9, 16, 25]

# print(squares + [1,2])

# for i in range(3):
#     print('8',end='')

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for i in users:
#     print(i)


# Conditions

# def t(s):
#     match s:
#         case 'hh'|2:
#             return 'Y'
#         case 1:
#             return 'N'
#         case _:
#             return 'nope'

# print(t(2))

# def h():
#     if 2==1:
#         return 1

# print(h()==None)

# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# print(parrot(1,'blink',type='ws'))

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])


# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


# Classes
# spam = '-_-'

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)


# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'
#     def __init__(self):
#         self.data = [1,2]

# print(MyClass.i)
# x = MyClass()
# print(x.data)



# class Complex:
#     def f(self,realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#         print("ehe")

# x = Complex.f(3.0, -4.5)
# print(x.r)
# #print(x.r, x.i)



# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#         print('ehe')

# x = Complex(1, -4.5)
# print(x.r, x.i)

# #x.r = 1
# while x.r < 10:
#     print(x.r)
#     x.r+=1
# print(x.r)
# #del x.counter


# class Dog:

#     kind = 'canine'         # class variable shared by all instances

#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance

# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.kind                  # shared by all dogs
# 'canine'
# >>> e.kind                  # shared by all dogs
# 'canine'
# >>> d.name                  # unique to d
# 'Fido'
# >>> e.name                  # unique to e
# 'Buddy'




# class Dog:

#     tricks = []             # mistaken use of a class variable

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# d.tricks     
# print(d.tricks)           # unexpectedly shared by all dogs
# # ['roll over', 'play dead']


# class Dog:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)
# ['roll over']
# print(e.tricks)
# ['play dead']


# class Warehouse:
#    purpose = 'storage'
#    region = 'west'

# w1 = Warehouse()
# print(w1.purpose, w1.region)

# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)

# print(w1.region)

# from dataclasses import dataclass

# @dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int

# john = Employee('john', 'computer lab', 1000)
# print(john.dept)

# print(john.salary)


class epr:
    pass

print(dir(epr))

object