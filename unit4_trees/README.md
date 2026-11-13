# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Completed Implementation

Author: Jerrell Rodgers

I created a One Piece-themed binary search tree using fictional
bounties measured in millions of berries.

I inserted seven values: 500, 300, 700, 200, 400, 600, and 800.
Smaller values were inserted recursively into the left subtree,
and larger values were inserted into the right subtree.
Duplicate values were ignored.

I performed an in-order traversal by visiting the left subtree,
the current node, and the right subtree. This produced the sorted
values: 200, 300, 400, 500, 600, 700, and 800.

## Testing and Edge Cases

I searched for 300 and 700, which returned True.
I searched for 250 and 900, which returned False.

I also tested an empty tree. Traversal returned an empty list,
and searching returned False. Inserting a duplicate bounty of
500 did not change the tree's contents.

The program completed successfully with exit code 0.

## Performance and Real World Application

The bounty index demonstrated how numeric records could be
organized and retrieved using a BST.

A balanced BST supported O(log n) searching because each comparison
eliminated one subtree from consideration. An unsorted list could
require O(n) comparisons.

However, inserting values in sequential order could create a
one-sided tree, making searches O(n). My implementation did not
automatically rebalance itself. In-order traversal took O(n)
because it visited every node.