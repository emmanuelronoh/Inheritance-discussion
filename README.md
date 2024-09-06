Inheritance in Object-Oriented Programming
1. Introduction to Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit properties and behaviors (methods) from another class. This promotes code reusability and establishes a natural hierarchy between classes.

2. Key Terms
Parent Class (Base Class, Superclass): The class whose properties and methods are inherited.
Child Class (Derived Class, Subclass): The class that inherits properties and methods from the parent class.
3. Benefits of Inheritance
Code Reusability: Child classes can reuse code from parent classes, reducing redundancy.
Extensibility: New functionality can be added to existing classes by creating new child classes.
Maintainability: Changes made to the parent class automatically propagate to child classes, simplifying updates and maintenance.
4. Syntax for Inheritance
In Python, inheritance is implemented by specifying the parent class in parentheses when defining the child class.

python
Copy code
class ParentClass:
    def __init__(self):
        self.parent_attribute = "Parent Attribute"

    def parent_method(self):
        print("This is a method from the Parent Class.")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the __init__ method of the ParentClass
        self.child_attribute = "Child Attribute"

    def child_method(self):
        print("This is a method from the Child Class.")
5. Types of Inheritance
Single Inheritance: A child class inherits from a single parent class.

python
Copy code
class A:
    pass

class B(A):
    pass
Multiple Inheritance: A child class inherits from more than one parent class.

python
Copy code
class A:
    pass

class B:
    pass

class C(A, B):
    pass
Multilevel Inheritance: A class is derived from another class, which is also derived from another class.

python
Copy code
class A:
    pass

class B(A):
    pass

class C(B):
    pass
Hierarchical Inheritance: Multiple classes inherit from a single parent class.

python
Copy code
class A:
    pass

class B(A):
    pass

class C(A):
    pass
Hybrid Inheritance: A combination of two or more types of inheritance.

6. Method Overriding
Child classes can provide specific implementations of methods that are already defined in their parent classes. This is called method overriding.

python
Copy code
class ParentClass:
    def show(self):
        print("Show from ParentClass")

class ChildClass(ParentClass):
    def show(self):
        print("Show from ChildClass")

obj = ChildClass()
obj.show()  # Output: Show from ChildClass
7. Using super()
super() is used to call methods from the parent class within the child class. This is useful for extending or modifying inherited methods.
python
Copy code
class ParentClass:
    def __init__(self):
        print("ParentClass __init__")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Calls ParentClass __init__
        print("ChildClass __init__")

obj = ChildClass()
# Output:
# ParentClass __init__
# ChildClass __init__
8. Conclusion
Inheritance allows for creating a new class based on an existing class, facilitating code reuse and establishing a logical relationship between classes. Understanding and effectively using inheritance is key to building scalable and maintainable object-oriented systems.