from AVLTree import AVLTree, AVLNode
from tests import tests
from graph_tree import draw_binary_tree

def main():
    test = tests()
    test.testInsertDelete()
    """
    tree = AVLTree()
    tree.insert(23,23)
    tree.insert(4,4)
    tree.insert(30,30)
    tree.insert(11,11)
    tree.insert(7,7)
    print(tree.avl_to_array())
    draw_binary_tree(tree.get_root())
    """
    print("end")


if __name__ == '__main__':
    main()
