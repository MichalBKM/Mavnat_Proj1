from AVLTree import AVLTree, AVLNode
from tests import tests
from graph_tree import draw_binary_tree

def main():
    test = tests()
    test.test_split()
    """
    t1 = AVLTree()
    t1.insert(12,12)
    t2 = AVLTree()
    t1.join(t2,10,10)
    print(draw_binary_tree(t1.get_root()))
    
    tree1 = AVLTree()
    tree1.insert(4,4)
    tree1.insert(2,2)
    tree1.insert(5,5)
    tree2 = AVLTree()
    tree2.insert(20,20)
    tree2.insert(16,16)
    tree2.insert(22,22)
    tree2.insert(14,14)
    tree2.insert(18,18)
    tree1.join(tree2,10,10)
    draw_binary_tree(tree1.get_root())
    #draw_binary_tree(tree2.get_root())
    """

    print("end")



if __name__ == '__main__':
    main()
