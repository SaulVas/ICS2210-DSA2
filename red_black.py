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
        new_node = self._insert(self.root, key)
        self._restore_rb_properties(new_node, self.root)

    def _insert(self, node, key):
        if node is None:
            new_node = RedBlackNode(key, is_red=True)
            return new_node

        if key < node.key:
            child = self._insert(node.left, key)
            node.left = child
            child.parent = node
        else:
            child = self._insert(node.right, key)
            node.right = child
            child.parent = node

        return child

    def _restore_rb_properties(self, node, root):
        if node.parent is None:
            node.red = False
            return node

        if not node.parent.red:
            return root

        parent = node.parent
        grandparent = parent.parent
        uncle = grandparent.left if grandparent.left != parent else grandparent.right

        if uncle and uncle.red:
            parent.red = False
            uncle.red = False
            grandparent.red = True
            return self._restore_rb_properties(grandparent, root)

        if parent == grandparent.left and node == parent.right:
            self._left_rotate(parent)
        elif parent == grandparent.right and node == parent.left:
            self._right_rotate(parent)

        if parent == grandparent.left:
            self._right_rotate(grandparent)
        else:
            self._left_rotate(grandparent)

        parent.red = False
        grandparent.red = True

        return root

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

    def _insert_steps_and_rotation(self, node, key):
        pass
