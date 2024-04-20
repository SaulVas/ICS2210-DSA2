"""
"""
from binary_tree import BinaryTree

class AVLNode:
    """
    
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return f"{self.key}"

    def set_height(self, new_height):
        """
        
        """
        self.height = new_height


class AVLTree(BinaryTree):
    """
    
    """
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

    def _rotate_left(self, node):
        right_tree = node.right
        node.right = right_tree.left
        right_tree.left = node

        # Reset heights
        node.set_height(1 + max(self._get_height(node.left), self._get_height(node.right)))
        right_tree.set_height(1 + max(self._get_height(right_tree.left),
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
