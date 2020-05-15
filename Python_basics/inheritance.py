""" Inheritance allows us to define a class that inherits all the methods
and properties from another class.

=> Parent class is the class being inherited from, also called base class.
=> Child class is the class that inherits from another class, 
also called derived class. """


class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass
    
x= Student("mike", "ocen")
x.printname()


"""
Python also has a super() function that will make the child class inherit 
all the methods and properties from its parent:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
   => super().__init__(fname, lname)

        adding new properties
        =>self.graduationyear = year

x = Student("Mike", "Olsen", 2020)
x.printname()

"""

"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
"""
