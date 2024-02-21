from AVLTree import AVLTree, AVLNode

def main():
    """
    tree1 = AVLTree()
    tree1.insert(70,0)
    tree1.insert(50,1)
    tree1.insert(80,2)
    tree1.insert(90,3)
    tree1.insert(40,4)
    tree1.insert(60,5)
    """
    tree2 = AVLTree()
    tree2.insert(2,0)
    tree2.insert(1,1)
    tree2.insert(3,2)
    a = tree2.search(2)
    tree2.split(a)
    #tree1.join(tree2,5,20)


if __name__ == '__main__':
    main()
