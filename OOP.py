"""def getName(firstName):
    a = firstName
    print("Hello", a)


print(getName('nadim'))

# Class and Constructor
class Person:

    def __init__(self, fname, lname):
        self.a = fname
        self.b = lname

    def getName(self):
        print("My Name is: ", self.a, self.b)


obj = Person('nadim', 'kaysar')
obj.getName()


# Class and Inheritance

class HTC:
    def call(self):
        print("Call Print")

    def message(self):
        print("Message print")


class SAMSANG(HTC):

    def photo(self):
        print("Print Photo")


class OPP(SAMSANG):

    def opp_photo(self):
        print("Oppo Photo")"""


# Method Overloading with dynamic
from hashlib import new


class A:
    def show(self):
        print("Base class")


class B(A):  # this would also work fine without deriving: class B:
    def show(self):
        print("Derived class")


obj = B()
obj.show()
