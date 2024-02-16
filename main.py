from AVLTree import AVLTree, AVLNode

def main():
    #node = AVLNode(10,3)
    #print(node)
    tree = AVLTree()
    tree.insert(10,0)
    tree.insert(5,1)
    tree.insert(4,2)
    tree.insert(80,3)
    tree.insert(19,4)
    tree.insert(6,5)
    tree.insert(2,6)
    print(tree.avl_to_array())
    #print(tree.get_root())
    #print(tree.size())
    #print(tree.search(1))
    a = tree.search(2)
    tree.delete(a)
    print(tree.size())
    #print(tree.avl_to_array())
    #print(tree.split(AVLNode(5,1)))

    print("end")

if __name__ == '__main__':
    main()
