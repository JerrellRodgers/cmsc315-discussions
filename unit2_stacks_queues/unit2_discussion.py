"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding to the end makes this the newest item on the stack (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Stack is empty. Nothing to remove."

        # LIFO: Remove the most recently added item first.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return "Stack is empty. Nothing to view."

        # Peek returns the newest item without removing it.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # FIFO: New items join the back, so older items are served first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the front value.
        # Handle an empty queue.
        if self.is_empty():
            return "Queue is empty. Nobody to serve."

        # FIFO: Remove the first item added.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return "Queue is empty. Nobody is waiting."

        # Return the first item without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0
def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

        # ===============================
        # TODO (Student): STACK DEMO
        # ===============================
        # Requirements:
        # 1. Create a Stack object.
        # 2. Add at least 4 values to the stack.
        # 3. Improve the print statements so they clearly explain what is happening.
        # 4. Demonstrate LIFO behavior.
        # 5. Show what happens when pop() is used on an empty stack.
        #
        # Edge Cases:
        # 6. Show what happens when peek() is used on an empty stack.
        # 7. Create a stack with only one item, remove it,
        #    and verify the stack is empty afterward.


    print("\n=== ZORO'S SWORD STACK ===")

    swords = Stack()

    # Add four swords to demonstrate LIFO.
    swords.push("Wado Ichimonji")
    swords.push("Sandai Kitetsu")
    swords.push("Enma")
    swords.push("Shusui")

    print("Zoro added four swords to his stack.")
    print("Top sword:", swords.peek())

    # LIFO: The last sword added is removed first.
    print("First sword removed:", swords.pop())
    print("Second sword removed:", swords.pop())
    print("Third sword removed:", swords.pop())
    print("Fourth sword removed:", swords.pop())

    # Edge case: Attempt to remove from an empty stack.
    print("Removing from empty stack:", swords.pop())

    # Edge case: Attempt to peek at an empty stack.
    print("Peeking at empty stack:", swords.peek())

    # Edge case: A stack containing only one item.
    single_sword = Stack()
    single_sword.push("Yubashiri")

    print("Single sword removed:", single_sword.pop())
    print("Is the single-item stack empty?", single_sword.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== SANJI'S FOOD QUEUE ===")

    food_line = Queue()

    # Add four pirates to the back of the queue.
    food_line.enqueue("Luffy")
    food_line.enqueue("Zoro")
    food_line.enqueue("Usopp")
    food_line.enqueue("Chopper")

    print("Four pirates are waiting for Sanji's food.")
    print("First pirate in line:", food_line.front())

    # FIFO: The first pirate to join the line is served first.
    print("First pirate served:", food_line.dequeue())
    print("Second pirate served:", food_line.dequeue())
    print("Third pirate served:", food_line.dequeue())
    print("Fourth pirate served:", food_line.dequeue())

    # Edge case: Attempt to serve someone when the queue is empty.
    print("Serving from empty queue:", food_line.dequeue())

    # Edge case: Attempt to view the front of an empty queue.
    print("Viewing empty queue:", food_line.front())

    # Edge case: A queue containing only one pirate.
    single_pirate = Queue()
    single_pirate.enqueue("Brook")

    print("Single pirate served:", single_pirate.dequeue())
    print("Is the single-item queue empty?", single_pirate.is_empty())
if __name__ == "__main__":
    main()
