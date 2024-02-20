from AVLTree import AVLTree, AVLNode

def main():
    tree = AVLTree()
    tree.insert(15, 0)
    tree.insert(10, 1)
    tree.insert(22, 2)
    tree.insert(4, 3)
    tree.insert(11, 4)
    tree.insert(20, 5)
    tree.insert(24, 6)
    tree.insert(2, 7)
    tree.insert(7, 8)
    tree.insert(12, 9)
    tree.insert(18, 10)
    tree.insert(1, 11)
    tree.insert(6, 12)
    tree.insert(8, 13)
    tree.insert(5, 14)

    tree1 = AVLTree()
    print(tree1.insert(8,0))
    print(tree1.insert(7,1))
    print(tree1.insert(6,2))
    #print(tree.avl_to_array())
    #print(tree.get_root())
    #print(tree.get_root().get_left())


if __name__ == '__main__':
    main()
