"""
    ICS2210 Project
"""

from random import randint
from statistics import mean, stdev, median
from AVL import AVLTree
from RedBlack import RedBlackTree
from SkipList import SkipList

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

    # initial insert
    avl_tree = AVLTree()
    rb_tree = RedBlackTree()
    skip_list = SkipList()
    for number in integers:
        avl_tree.insert(number)
        rb_tree.insert(number)
        skip_list.insert(number)

    # Insertion of Second array
    second_integers = [randint(1, 100000) for _ in range(1001)]

    # AVL Tree section
    insertion_steps = {
        "avl": [],
        "rb": [],
        "skip_list": []
        }
    rotations = {
        "avl": [],
        "rb": [],
        }
    promotions = []
    for num in second_integers:
        steps, rotation = avl_tree.insertion_steps_and_rotation(num)
        insertion_steps["avl"].append(steps)
        rotations["avl"].append(rotation)

        steps, rotation = rb_tree.insertion_steps_and_rotation(num)
        insertion_steps["rb"].append(steps)
        rotations["rb"].append(rotation)

        steps, promotion = skip_list.insert_steps_and_promotions(num)
        insertion_steps["skip_list"].append(steps)
        promotions.append(promotion)


    print("AVL Tree Insertion Steps Statistics:")
    print(f"Minimum: {min(insertion_steps["avl"])}")
    print(f"Maximum: {max(insertion_steps["avl"])}")
    print(f"Mean: {mean(insertion_steps["avl"])}")
    print(f"Standard Deviation: {stdev(insertion_steps["avl"])}")
    print(f"Median: {median(insertion_steps["avl"])}\n")

    print("AVL Tree Rotations Statistics:")
    print(f"Minimum: {min(rotations["avl"])}")
    print(f"Maximum: {max(rotations["avl"])}")
    print(f"Mean: {mean(rotations["avl"])}")
    print(f"Standard Deviation: {stdev(rotations["avl"])}")
    print(f"Median: {median(rotations["avl"])}\n")

    print(f"AVL Tree Height: {avl_tree.root.height}")
    print(f"AVL Tree Leaves: {avl_tree.get_leaves()}\n")

    print("RB Tree Insertion Steps Statistics:")
    print(f"Minimum: {min(insertion_steps["rb"])}")
    print(f"Maximum: {max(insertion_steps["rb"])}")
    print(f"Mean: {mean(insertion_steps["rb"])}")
    print(f"Standard Deviation: {stdev(insertion_steps["rb"])}")
    print(f"Median: {median(insertion_steps["rb"])}\n")

    print("RB Tree Rotations Statistics:")
    print(f"Minimum: {min(rotations["rb"])}")
    print(f"Maximum: {max(rotations["rb"])}")
    print(f"Mean: {mean(rotations["rb"])}")
    print(f"Standard Deviation: {stdev(rotations["rb"])}")
    print(f"Median: {median(rotations["rb"])}\n")

    print(f"RB Tree Height: {rb_tree.get_height()}")
    print(f"RB Tree Leaves: {rb_tree.get_leaves()}")

    print("Skip List Insertion Steps Statistics:")
    print(f"Minimum: {min(insertion_steps["skip_list"])}")
    print(f"Maximum: {max(insertion_steps["skip_list"])}")
    print(f"Mean: {mean(insertion_steps["skip_list"])}")
    print(f"Standard Deviation: {stdev(insertion_steps["skip_list"])}")
    print(f"Median: {median(insertion_steps["skip_list"])}\n")

    print("Skip List Promotions Statistics:")
    print(f"Minimum: {min(promotions)}")
    print(f"Maximum: {max(promotions)}")
    print(f"Mean: {mean(promotions)}")
    print(f"Standard Deviation: {stdev(promotions)}")
    print(f"Median: {median(promotions)}\n")

    print(f"Skip List Levels: {skip_list.max_height}")
