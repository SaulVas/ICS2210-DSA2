"""
    ICS2210 Project
"""

from random import randint
from avl import AVLTree

def knuth_shuffle(array):
    """
    Shuffles the elements of the given array using the Knuth Shuffle algorithm.
    
    Parameters:
    array (list): The array to be shuffled.
    
    Returns:
    None. The array is shuffled in-place.
    """
    for index in range(len(array) - 1, 0, -1):
        swap_index = randint(0, index)
        array[index], array[swap_index] = array[swap_index], array[index]

if __name__ == "__main__":
    integers = list(range(1, 5001))
    knuth_shuffle(integers)

    # AVL Tree section
    avl_tree = AVLTree()
    for number in integers:
        avl_tree.insert(number)
