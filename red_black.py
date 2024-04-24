from binary_tree import BinaryTree

class RedBlackNode:
    def __init__(self, key, is_red=True):
        self.key = key
        self.red = is_red
        self.left = None
        self.right = None
        self.parent = None

    def is_red(self):
        return self.red

class RedBlackTree(BinaryTree):
    def insert(self, key):
        self._insert(None, self.root, key)

    def _insert(self, parent, node, key):
        if node is None:
            node = RedBlackNode(key)
            node.parent = parent
            if parent:
                if key < parent.key:
                    parent.left = node
                else:
                    parent.right = node
            self._restore_rb_properties(node)
        elif key < node.key:
            self._insert(node, node.left, key)
        else:
            self._insert(node, node.right, key)

    def _restore_rb_properties(self, node):
        # base case, node is root
        if node.parent is None:
            node.red = False
            self.root = node
            return node

        # parent is black, no action needed
        if not node.parent.red:
            return node

        parent = node.parent
        grandparent = parent.parent

        if grandparent:
            uncle = grandparent.left if grandparent.left != parent else grandparent.right
        else:
            uncle = None

        # case 1: uncle is red
        if uncle and uncle.red:
            parent.red = False
            uncle.red = False
            grandparent.red = True
            self._restore_rb_properties(grandparent)
            return node

        # case 2: uncle is black
        if grandparent and parent == grandparent.left and node == parent.right:
            self._left_rotate(parent)
        elif grandparent and parent == grandparent.right and node == parent.left:
            self._right_rotate(parent)

        parent = node

        if grandparent and parent.key < grandparent.key:
            self._right_rotate(grandparent)
        elif grandparent and parent.key >= grandparent.key:
            self._left_rotate(grandparent)

        parent.red = not parent.red
        if grandparent:
            grandparent.red = not grandparent.red


        self._restore_rb_properties(grandparent)

        return node

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left:
            right_child.left.parent = node

        right_child.parent = node.parent

        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right:
            left_child.right.parent = node

        left_child.parent = node.parent

        if not node.parent:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        left_child.right = node
        node.parent = left_child

    def insertion_steps_and_rotation(self, key):
        new_node, steps = self._insert_steps(self.root, key)
        self.root, rotations = self._restore_rb_properties_tracking_rotations(new_node,
                                                                              self.root, 0)
        return (steps, rotations)

    def _insert_steps(self, node, key):
        if node is None:
            return (RedBlackNode(key), 0)

        if key < node.key:
            (child, steps) = self._insert_steps(node.left, key)
            node.left = child
            child.parent = node
        else:
            (child, steps) = self._insert_steps(node.right, key)
            node.right = child
            child.parent = node

        return (child, steps + 1)

    def _restore_rb_properties_tracking_rotations(self, node, root, rotations):
        rotations_this_call = 0
        if node.parent is None:
            node.red = False
            return (node, rotations)

        if not node.parent.red:
            return (root, rotations)

        parent = node.parent
        grandparent = parent.parent
        uncle = grandparent.left if grandparent.left != parent else grandparent.right

        if uncle and uncle.red:
            parent.red = False
            uncle.red = False
            grandparent.red = True
            return self._restore_rb_properties_tracking_rotations(grandparent, root, rotations)

        if parent == grandparent.left and node == parent.right:
            self._left_rotate(parent)
            rotations += 1
            rotations_this_call += 1
        elif parent == grandparent.right and node == parent.left:
            self._right_rotate(parent)
            rotations += 1
            rotations_this_call += 1

        if parent == grandparent.left:
            self._right_rotate(grandparent)
            if rotations_this_call == 0:
                rotations += 1
        else:
            self._left_rotate(grandparent)
            if rotations_this_call == 0:
                rotations += 1

        parent.red = False
        grandparent.red = True

        return (root, rotations)

    def is_rb_tree(self):
        return self._is_rb_tree(self.root)[0]

    def _is_rb_tree(self, node):
        if not node:
            return True, 1

        if not node.parent and node.red:
            return False, 0

        if node.red:
            num_blacks = 0
            if (node.left and node.left.red) or (node.right and node.right.red):
                return False, -1
        else:
            num_blacks = 1

        right, num_blacks_right = self._is_rb_tree(node.right)
        left, num_blacks_left = self._is_rb_tree(node.left)

        return all([right, left, num_blacks_right == num_blacks_left]), num_blacks_right + num_blacks