"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    world = "One Piece"

    def __init__(self, name, bounty):
        self.name = name
        self.bounty = bounty
    def increase_bounty(self, amount):
        if amount < 0:
            raise ValueError("Bounty increase cannot be negative")

        self.bounty += amount
        return f"{self.name}'s new bounty is {self.bounty:,} berries"

    def display_info(self):
        return f"Pirate: {self.name}, Bounty: {self.bounty:,} berries"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    category = "Devil Fruit User"

    def __init__(self, name, bounty, devil_fruit, crew):
        super().__init__(name, bounty)
        self.devil_fruit = devil_fruit
        self.crew = crew

    def use_power(self):
        return f"{self.name} uses the power of the {self.devil_fruit}!"

    def display_info(self):
        return f"{super().display_info()}, Devil Fruit: {self.devil_fruit}, Crew: {self.crew}"
# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    luffy = ChildClass("Luffy", 3000000000, "Gomu Gomu no Mi", "Straw Hat Pirates")
    doflamingo = ChildClass("Doflamingo", 340000000, "Ito Ito no Mi", "Donquixote Pirates")

    print("Class variable:", ChildClass.category)
    print("Access through object:", luffy.category)

    luffy.gear = "Gear 5"

    print("Luffy's namespace:", luffy.__dict__)
    print("Doflamingo's namespace:", doflamingo.__dict__)
    print("Class namespace:", list(ChildClass.__dict__.keys()))

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    luffy = ChildClass("Luffy", 3000000000, "Gomu Gomu no Mi", "Straw Hat Pirates")

    luffy.inventory = ["Sword", "Treasure Map", "Meat"]

    shallow_luffy = copy(luffy)
    deep_luffy = deepcopy(luffy)

    # A shallow copy shares references to nested mutable objects.
    # A deep copy creates independent copies of nested mutable objects.

    luffy.inventory.append("Devil Fruit")

    print("Original inventory:", luffy.inventory)
    print("Shallow copy inventory:", shallow_luffy.inventory)
    print("Deep copy inventory:", deep_luffy.inventory)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    zoro = ParentClass("Zoro", 1111000000)
    print(zoro.display_info())
    print(zoro.increase_bounty(500000000))

    print("\n=== Child Object ===")
    luffy = ChildClass(
        "Luffy",
        3000000000,
        "Gomu Gomu no Mi",
        "Straw Hat Pirates"
    )

    print(luffy.display_info())
    print(luffy.use_power())

    demonstrate_namespaces()
    demonstrate_copying()
if __name__ == "__main__":
    main()