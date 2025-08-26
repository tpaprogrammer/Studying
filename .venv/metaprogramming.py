"""
This file executes an example of creating a new metaclass based on a class defined
using the standard 'class' keyword.
"""


def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()

print()
print("*" * 20)
print("End of first example code block.")
print("*" * 20)
print()
print()

"""
The 'Dog' class is now equipped with two methods (feed() and bark()) and the instance
    attribute 'age'.
"""

"""
The metaclass is created by line 14, notably using the 'type' keyword.

This mirrors a portion of Python's creation process for a new class using the 'class'
    keyword, specifically the end portion. Upon creating a class using the 'class' key and
    instantiating an object based on that class:

    1. The 'class' instruction is identified and the class body is executed.
    2. " 'class' = 'type(, , )' " is executed.
    3. 'type(, , )' is responsible for calling the '__call__' method upon class
           instance creation. The '__call__' method calls two other methods, in order:
        
        a. First '__new__()', responsible for creating the class instance in the computer
               memory
        b. Then '__init__()', which is responsible for object initialization.
"""

"""
Metaclasses usually implement these two methods (__init__ & __new__), taking control of
    the procedure of creating and initializing a new class instance. As a result, classes
    receive a new layer of logic.
"""

"""
It’s important to remember that metaclasses are classes that are instantiated
    to get classes.
"""

"""
What follows is a full implementation of a new metaclass.
"""

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj

class My_Object(metaclass=My_Meta):
    pass

print(My_Object.__dict__)

"""
- The class 'My_Meta' is derived from 'type'. This makes the class a metaclass.
- A new '__new__' method has been defined. Note: '__new__' is an inherent, special
    method which is called before the __init__ method in the normal course of creating
    a class using the 'class' keyword. It can be overridden, as is done here.
- The role of the new '__new__' method is to call the __new__ method of the parent class
    to create a new class. Note the use of 'super()' in line 71.
- The '__new__' method uses 'mcs' as an argument to refer to the class ('mcs' is a
    convention).
- Line 72 is an example of the format used to create an attribute in the new class.
"""

"""
Summary of the second code block example:

- A new class has been defined in a way where a custom metaclass is listed in the class
    definition as a metaclass. This is a way to tell Python to use 'My_Meta' as a
    metaclass, not as an ordinary superclass.
- The contents of the new class' "__dict__" attribute are printed to check if the custom
    attribute is present.
"""

"""
Considering reviewing PCPP 5.1.1.9 and walking through the example code block.
"""