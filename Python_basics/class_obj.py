"""To understand the meaning of classes we have to understand the 
built-in __init__() function.
All classes have a function called __init__(), which is always executed 
when the class is being initiated.
Use the __init__() function to assign values to object properties, or 
other operations that are necessary to do when the object is being 
created: """

"""
class Person:
    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Nikita', 26)
print('hello my name is ' + p.name)
print(+p.age)
"""


"""The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class """

class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        p = person1('john', 34)
        p.myfunc()

    def myfunc(self):
        print('hello my name is ' + self.name)