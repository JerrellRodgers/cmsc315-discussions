"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the character at the requested position.
    # Existing characters shift right to make space.
    # Inserting near the beginning takes more work
    # than inserting at the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check that the index exists before removing anyone.
    # This prevents an IndexError.
    if 0 <= index < len(lst):
        return lst.pop(index)

    # Return None if the position is invalid.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks each character in order.
    for index, character in enumerate(lst):
        if character == value:
            return index

    # Return -1 if the character was not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

crew = ["Zoro", "Nami", "Sanji"]
print("Original crew:", crew)

# Add Luffy at the beginning.
insert_at(crew, 0, "Luffy")
print("After adding Luffy:", crew)

# Add Usopp in the middle.
insert_at(crew, 2, "Usopp")
print("After adding Usopp:", crew)

# Add Chopper at the end.
insert_at(crew, len(crew), "Chopper")
print("After adding Chopper:", crew)
    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

print("\n=== DELETION TESTS ===")

# Remove the first crew member.
removed = delete_at(crew, 0)
print("Removed from beginning:", removed)
print("Crew:", crew)

# Remove a character from the middle.
removed = delete_at(crew, len(crew) // 2)
print("Removed from middle:", removed)
print("Crew:", crew)

# Remove the last crew member.
removed = delete_at(crew, len(crew) - 1)
print("Removed from end:", removed)
print("Crew:", crew)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

print("\n=== SEARCH TESTS ===")
# Search for Zoro, who is in our crew.
print("Zoro found at index:", search_value(crew, "Zoro"))

# Shanks is not a Straw Hat crew member.
print("Shanks found at index:", search_value(crew, "Shanks"))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

print("\n=== EDGE CASES ===")
# Edge case 1: Invalid deletion index.
print("Invalid deletion:", delete_at(crew, 100))

# Edge case 2: Delete from an empty list.
empty_crew = []
print("Delete from empty crew:", delete_at(empty_crew, 0))

# Edge case 3: Insert into an empty list.
insert_at(empty_crew, 0, "Brook")
print("New crew:", empty_crew)



if __name__ == "__main__":
    main()