"""
    ICS2210 Project
"""

from random import randint
from statistics import mean, stdev, median
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
    # Insertion of First array
    integers = list(range(1, 5001))
    knuth_shuffle(integers)

    # AVL Tree section
    avl_tree = AVLTree()
    for number in integers:
        avl_tree.insert(number)


    # Insertion of Second array
    second_integers = [randint(1, 100000) for _ in range(1001)]

    # AVL Tree section
    insertion_steps = []
    rotations = []
    for num in second_integers:
        steps, rotation = avl_tree.insertion_steps_and_rotation(num)
        insertion_steps.append(steps)
        rotations.append(rotation)

    print("Insertion Steps Statistics:")
    print(f"Minimum: {min(insertion_steps)}")
    print(f"Maximum: {max(insertion_steps)}")
    print(f"Mean: {mean(insertion_steps)}")
    print(f"Standard Deviation: {stdev(insertion_steps)}")
    print(f"Median: {median(insertion_steps)}\n")

    print("Rotations Statistics:")
    print(f"Minimum: {min(rotations)}")
    print(f"Maximum: {max(rotations)}")
    print(f"Mean: {mean(rotations)}")
    print(f"Standard Deviation: {stdev(rotations)}")
    print(f"Median: {median(rotations)}\n")

    print(f"Tree Height: {avl_tree.root.height}")
    print(f"Leaves: {avl_tree.get_leaves()}")
