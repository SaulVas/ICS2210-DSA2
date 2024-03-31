"""
This module defines the AVLTree class, which represents an AVL Tree data structure.

An AVL Tree is a self-balancing binary search tree, where the heights of the left and right subtrees
of any node differ by at most one.

Classes:
    AVKLNode: A class representing a Node in an AVL tree
    AVLTree: A class representing an AVL Tree data structure.

"""

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
