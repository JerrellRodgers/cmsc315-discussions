"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Smaller values go left; larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position becomes a new node.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Each comparison skips the subtree that cannot contain the value.
        # Balanced trees search in O(log n); skewed trees can take O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # An empty branch means the value was not found.
        if node is None:
            return False

        # Stop searching when the value matches.
        if value == node.value:
            return True

        # Search only the side where the value could exist.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Collect the values in sorted order.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # Left values are smaller, so visit them first.
            self._inorder_recursive(node.left, values)

            # Visit this node before its larger right-side values.
            values.append(node.value)

            self._inorder_recursive(node.right, values)

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # TODO: Create a BST and insert multiple values.
    tree = BST()

    # Fictional One Piece training bounties in millions of berries.
    bounties = [500, 300, 700, 200, 400, 600, 800]

    # Starting near the middle creates a balanced example.
    # Each comparison skips the subtree that cannot contain the value.
    for bounty in bounties:
        tree.insert(bounty)

    print("Bounties inserted:", bounties)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # TODO: Display and explain traversal results.
    print("Bounties in sorted order:", tree.inorder())

    # Visiting left, current, then right produces ascending order.
    print("In-order traversal lists the bounties from lowest to highest.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # TODO: Demonstrate BST searching.
    # These two bounties were inserted, so both searches return True.
    print("Search for 300:", tree.search(300))
    print("Search for 700:", tree.search(700))

    # These two bounties were never inserted, so both return False.
    print("Search for 250:", tree.search(250))
    print("Search for 900:", tree.search(900))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")    # TODO: Demonstrate and explain an edge case.
    empty_tree = BST()

    # An empty tree has no values to traverse or find.
    print("Empty tree traversal:", empty_tree.inorder())
    print("Search empty tree for 500:", empty_tree.search(500))

    # Duplicate bounties are ignored, so the tree stays unchanged.
    tree.insert(500)
    print("After inserting duplicate 500:", tree.inorder())



if __name__ == "__main__":
    main()