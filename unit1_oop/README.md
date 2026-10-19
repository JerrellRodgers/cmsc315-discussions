# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
## Implementation Summary

For this assignment, I created a One Piece-themed Python program that demonstrated object-oriented programming concepts.

I created a parent class that stored a pirate's name and bounty. I then created a child class that inherited those attributes and added information about Devil Fruits and pirate crews.

I demonstrated namespaces by creating objects for Luffy and Doflamingo and using `__dict__` to examine their attributes.

I demonstrated shallow and deep copying by creating copies of Luffy's inventory. After modifying the original inventory, I observed that the shallow copy reflected the changes while the deep copy remained unchanged.

For my student-created extension, I added a method that increased a pirate's bounty and rejected negative values using error handling.

I tested the program using characters from One Piece to demonstrate inheritance, method overriding, and object behavior.

## Testing

I ran the Python program in IntelliJ IDEA and tested the bounty increase functionality. The program successfully demonstrated class inheritance, namespaces, and the differences between shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.## Reflection

For this assignment, I learned how object-oriented programming works in Python, particularly inheritance, namespaces, and shallow versus deep copying. I created a One Piece-themed program using pirate characters to demonstrate these concepts. My parent class stored basic pirate information, while my child class inherited those attributes and added new functionality.

One challenge I encountered was understanding Python's syntax, especially indentation, constructors, and the use of `self`. I worked through these issues by reviewing error messages, correcting my code, and testing the program.

Compared to procedural programming, OOP organizes code into classes and objects rather than relying primarily on functions. This makes programs easier to maintain and allows developers to reuse existing code. However, OOP also introduces additional complexity and overhead when creating and managing classes, which may not be necessary for smaller programs.

I can see OOP being useful when developing applications that manage users, inventories, or other related information. Learning these concepts will help me build more organized, reusable, and maintainable programs in future projects.