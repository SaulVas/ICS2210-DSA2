from abc import ABC, abstractmethod

class BinaryTree(ABC):
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def traverse(self, string):
        """
        Traverses the  tree in the specified order.

        Parameters:
        - string (str): The traversal order. Valid values are 
        "in_order", "post_order", and "pre_order".

        Returns:
        - None

        Raises:
        - None
        """
        if string.lower() == "in_order":
            self._in_order_traversal(self.root)
        elif string.lower() == "post_order":
            self._post_order_traversal(self.root)
        elif string.lower() == "pre_order":
            self._pre_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if not node:
            return
        self._in_order_traversal(node.left)
        print(node.key)
        self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        if not node:
            return
        print(node.key)
        self._pre_order_traversal(node.left)
        self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        if not node:
            return
        self._post_order_traversal(node.left)
        self._post_order_traversal(node.right)
        print(node.key)

    def is_binary_tree(self):
        return self._is_binary_tree(self.root)

    def _is_binary_tree(self, node):
        if node is None:
            return True

        if node.left and node.left.key >= node.key:
            return False

        if node.right and node.right.key <= node.key:
            return False

        left_is_binary = self._is_binary_tree(node.left)
        right_is_binary = self._is_binary_tree(node.right)

        return left_is_binary and right_is_binary

    def search(self, key):
        """
        Search for a node with the given key in the tree.

        Parameters:
        - key: The key to search for.

        Returns:
        - True if found and False if otherwise
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        if key < node.left:
            return self._search(node.left, key)

        return self._search(node.right, key)

    @abstractmethod
    def insert(self, key):
        """
        Inserts a new key into the Tree.

        Args:
            key: The key to be inserted into the Tree.
        """

    def get_leaves(self):
        """
        Returns the number of leaves in the tree.

        Returns:
            int: The number of leaves in the tree.
        """
        leaves = 0
        return self._get_leaves(self.root, leaves)

    def _get_leaves(self, node, count):
        if not node:
            return count
        if node.left is None and node.right is None:
            return count + 1

        new_count = self._get_leaves(node.left, count)
        return self._get_leaves(node.right, new_count)

    @abstractmethod
    def insertion_steps_and_rotation(self, key):
        """
        Perform an insertion of a key into the tree and return the number 
        of steps taken and whether a rotation was performed or not.

        Parameters:
        - key: The key to be inserted into the tree.

        Returns:
        A tuple containing the number of steps taken during the 
        insertion process and 1 if a rotation occured or 0 otherwise.
        """
