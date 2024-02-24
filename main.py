from AVLTree import AVLTree, AVLNode
from tests import tests
from graph_tree import draw_binary_tree
from UnitTestAVLTree import TestAVLTree
import random

"""
start = 1
i=5
end = 1000*(2**i)
n = 1000*(2**i)
random_numbers = random.sample(range(start, end+1), n)
"""

def exp(i):
    AVLTree.costs = []
    tree1 = AVLTree()
    tree2 = AVLTree()

    start = 1
    end = 1000 * (2 ** i)
    n = 1000 * (2 ** i)
    random_numbers = random.sample(range(start, end + 1), n)
    cand = random_numbers

    #part 1 - splitting based on random key
    #print("split based on random key:")
    for item in cand:
        tree1.insert(item, 1)

    #max_left = tree1.get_root().get_left().get_max()
    #print(max_left)
    split_key = cand[random.randint(1,end+1)]
    #print("split key",split_key)
    item = tree1.search(split_key)
    left, right = tree1.split(item)

    #print("costs:",tree1.costs)
    #print(f"avg_cost = {sum(tree1.costs)/len(tree1.costs)}, max_cost = {max(tree1.costs)}")

    rand_avg = sum(tree1.costs)/len(tree1.costs)
    rand_max = max(tree1.costs)

    #part 2 - splitting based on the max_left key
    #print("\nsplit based on max_left key:")
    for item in cand:
        tree2.insert(item, 1)

    max_left = tree2.get_root().get_left().get_max()
    #print("max key",max_left)
    item = tree2.search(max_left)
    left, right = tree2.split(item)

    #print("costs: ",tree2.costs)
    #print(f"avg_cost = {sum(tree2.costs) / len(tree2.costs)}, max_cost = {max(tree2.costs)}")

    maxleft_avg = sum(tree2.costs) / len(tree2.costs)
    maxleft_max = max(tree2.costs)

    return [rand_avg,rand_max,maxleft_avg,maxleft_max]

def main():
    rand_avg = 0
    rand_max = 0
    maxleft_avg = 0
    maxleft_max = 0
    res = []


    tmp_res = exp(10)
    rand_avg = tmp_res[0]
    rand_max = tmp_res[1]
    maxleft_avg = tmp_res[2]
    maxleft_max = tmp_res[3]

    print(rand_avg,rand_max,maxleft_avg,maxleft_max)


if __name__ == '__main__':
    main()
