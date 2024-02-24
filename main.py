from AVLTree import AVLTree, AVLNode
from tests import tests
from graph_tree import draw_binary_tree
from UnitTestAVLTree import TestAVLTree

def main():
    t = TestAVLTree()
    t.test_avl_delete_node_with_two_children_ten()
    #t = tests()
    #t.test_avl_to_array()

    """
    avl_tree = AVLTree()
    avl_tree.insert(15, "15")
    avl_tree.insert(8, "8")
    avl_tree.insert(22, "22")
    avl_tree.insert(4, "4")
    avl_tree.insert(20, "20")
    avl_tree.insert(11, "11")
    avl_tree.insert(24, "24")
    avl_tree.insert(2, "2")
    avl_tree.insert(18, "18")
    avl_tree.insert(12, "12")
    avl_tree.insert(9, "9")
    avl_tree.insert(13, "13")
    #draw_binary_tree(avl_tree.get_root())
    avl_tree.delete(avl_tree.search(24))
    draw_binary_tree(avl_tree.get_root())
    """
    print("end")



if __name__ == '__main__':
    main()
