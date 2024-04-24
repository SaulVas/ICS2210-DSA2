from binary_tree import BinaryTree

class RedBlackNode:
    def __init__(self, key, is_red=True, parent=None):
        self.key = key
        self.red = is_red
        self.left = None
        self.right = None
        self.parent = parent

    def is_red(self):
        return self.red

class RedBlackTree(BinaryTree):
    def insert(self, key):
        self._insert(self.root, key)

    def _insert(self, node, key):
        parent = None
        current_node = node
        while True:
            # insert here
            if current_node is None:
                current_node = RedBlackNode(key, parent=parent)
                # new node is root
                if not current_node.parent:
                    current_node.red = False
                    self.root = current_node
                else:
                    # set parents pointer to new node
                    if current_node.key < parent.key:
                        parent.left = current_node
                    else:
                        parent.right = current_node
                    # check for conflicts
                    if parent.red:
                        self._resolve_problems(current_node)

                break

            parent = current_node.parent

            # remove red uncles
            if not current_node.red:
                # black node with red children
                if current_node.left and current_node.left.red:
                    if current_node.right and current_node.right.red:
                        current_node.left.red = False
                        current_node.right.red = False
                        if parent:
                            current_node.red = True

                        # check for red red violations and then rotate
                        if parent and parent.red:
                            self._resolve_problems(current_node)

            parent = current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

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

    def _resolve_problems(self, node):
        parent = node.parent

        if not parent.red:
            return

        grandparent = parent.parent

        # check for inside
        if parent is grandparent.left and node is parent.right:
            self._left_rotate(parent)
            parent = node
        elif parent is grandparent.right and node is parent.left:
            self._right_rotate(parent)
            parent = node

        # check for outside
        if parent is grandparent.left:
            self._right_rotate(grandparent)
            parent.red = not parent.red
            grandparent.red = not grandparent.red
        elif parent is grandparent.right:
            self._left_rotate(grandparent)
            parent.red = not parent.red
            grandparent.red = not grandparent.red

        if not parent.parent:
            self.root = parent
            parent.red = False

    def insertion_steps_and_rotation(self, key):
        pass

    def _insert_steps(self, node, key):
        pass

    def _restore_rb_properties_tracking_rotations(self, node, root, rotations):
        pass

    def is_rb_tree(self):
        return self._is_rb_tree(self.root)[0]

    def _is_rb_tree(self, node):
        if not node:  # if node is a leaf, check #3
            return True, 1

        if not node.parent and node.red:  # If node is the root, check #2
            return False, 0

        if node.red:  # if node is red, check #4
            n_blacks = 0
            if (node.left and node.left.red) or (node.right and node.right.red):
                return False, -1
        else:  # else, the number of black nodes to the leaves includes the same node
            n_blacks = 1

        # Check the subtrees for #5
        right, n_blacks_right = self._is_rb_tree(node.right)
        left, n_blacks_left = self._is_rb_tree(node.left)

        return all([right, left, n_blacks_right == n_blacks_left]), n_blacks_right + n_blacks
