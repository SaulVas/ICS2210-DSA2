from random import randint

class SkipNode:
    def __init__(self, height = 1, value = None):
        self.value = value
        self.next = [None] * height
        self.previous = [None] * height

    def __lt__(self, other):
        if isinstance(other, SkipNode):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, SkipNode):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, SkipNode):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, SkipNode):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, SkipNode):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, SkipNode):
            return self.value != other.value
        elif isinstance(other, int):
            return self.value != other
        return NotImplemented

class Head(SkipNode):
    def __lt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return False

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

class SkipList:
    def __init__(self):
        self.head = Head()
        self.len = 0
        self.max_height = 0

    def __len__(self):
        return self.len

    def _get_new_height(self):
        height = 1
        while randint(0, 1) == 0:
            height += 1
        return height

    def insert(self, value):
        new_node = SkipNode(self._get_new_height(), value)
        head = self.head

        # update max height and head next values
        self.max_height = max(self.max_height, len(new_node.next))
        while len(head.next) < len(new_node.next):
            head.next.append(None)
            head.previous.append(None)

        # find the correct place at each level
        current_node = self.head
        for level in reversed(range(self.max_height)):
            while current_node.next[level] and current_node.next[level] < value:
                current_node = current_node.next[level]

            # update next and previous pointers
            new_node.previous[level] = current_node
            new_node.next[level] = current_node.next[level]
            current_node.next[level] = new_node
            # Node isn't at the end of a list
            if new_node.next[level]:
                next_node = new_node.next[level]
                next_node.previous[level] = new_node
