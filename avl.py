"""
This module defines the AVLTree class, which represents an AVL Tree data structure.

An AVL Tree is a self-balancing binary search tree, where the heights of the left and right subtrees
of any node differ by at most one.

Classes:
    AVKLNode: A class representing a Node in an AVL tree
    AVLTree: A class representing an AVL Tree data structure.

"""

from typing import Any


class AVLNode:
    """
    Represents a node in an AVL tree.

    Attributes:
        key: The key value stored in the node.
        left: The left child of the node.
        right: The right child of the node.
        height: The height of the node in the AVL tree.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def set_height(self, new_height):
        """
        Sets the height of the node.

        Args:
            new_height (int): The new height value to be set.
        """
        self.height = new_height


class AVLTree:
    """
    A class representing an AVL Tree data structure.

    Attributes:
        root (AVLNode): The root node of the AVL Tree.

    Methods:
        insert(key): Inserts a new key into the AVL Tree.
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Inserts a new key into the AVL Tree.

        Args:
            key: The key to be inserted into the AVL Tree.
        """
        self.root = self._insert(self.root, key)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _rotate_left(self, node):
        right_tree = node.right
        node.right = right_tree.left
        right_tree.left = node

        # Reset heights
        node.set_height(1 + max(self._get_height(node.left), self._get_height(node.right)))
        right_tree.set_height(1 +
                              max(self._get_height(right_tree.left),
                                  self._get_height(right_tree.right)))

        return right_tree

    def _rotate_right(self, node):
        left_tree = node.left
        node.left = left_tree.right
        left_tree.right = node

        # Reset heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        left_tree.height = 1 + max(self._get_height(left_tree.left),
                                   self._get_height(left_tree.right))

        return left_tree

    def _insert(self, node, key):
        # Rec cases
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        # Adjust heights of nodes after insertion and check balancing condition
        height_left = self._get_height(node.left)
        height_right = self._get_height(node.right)
        node.set_height(1 + max(height_left, height_right))
        bal_factor = height_left - height_right

        # Perform rotations if required
        if bal_factor > 1:
            # LL or LR
            if key < node.left.key:
                return self._rotate_right(node)

            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if bal_factor < -1:
            # RR or RL
            if key >= node.right.key:
                return self._rotate_left(node)

            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insertion_steps_and_rotation(self, key):
        """
        Perform an insertion of a key into the AVL tree and return the number 
        of steps taken and whether a rotation was performed or not.

        Parameters:
        - key: The key to be inserted into the AVL tree.

        Returns:
        A tuple containing the number of steps taken during the 
        insertion process and 1 if a rotation occured or 0 otherwise.
        """
        self.root, steps, rotation = self._insert_steps_and_rotation(self.root, key)
        return (steps, rotation)

    def _insert_steps_and_rotation(self, node, key):
        # Rec cases
        if node is None:
            return (AVLNode(key), 0, 0)
        if key < node.key:
            (node.left, steps, rotation) = self._insert_steps_and_rotation(node.left, key)
        else:
            (node.right, steps, rotation) = self._insert_steps_and_rotation(node.right, key)

        # Adjust heights of nodes after insertion and check balancing condition
        height_left = self._get_height(node.left)
        height_right = self._get_height(node.right)
        node.set_height(1 + max(height_left, height_right))
        bal_factor = height_left - height_right

        # Perform rotations if required
        if bal_factor > 1:
            # LL or LR
            if key < node.left.key:
                return (self._rotate_right(node), steps + 1, rotation + 1)

            node.left = self._rotate_left(node.left)
            return (self._rotate_right(node), steps + 1, rotation + 1)
        if bal_factor < -1:
            # RR or RL
            if key >= node.right.key:
                return (self._rotate_left(node), steps + 1, rotation + 1)

            node.right = self._rotate_right(node.right)
            return (self._rotate_left(node), steps + 1, rotation + 1)

        return (node, steps + 1, rotation)

    def get_leaves(self):
        """
        Returns the number of leaves in the AVL tree.

        Returns:
            int: The number of leaves in the AVL tree.
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

    def traverse(self, string):
        """
        Traverses the AVL tree in the specified order.

        Parameters:
        - string (str): The traversal order. Valid values are "in_order", "post_order", and "pre_order".

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

    def search(self, key):
        """
        Search for a node with the given key in the AVL tree.

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
