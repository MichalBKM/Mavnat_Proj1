from AVLTree import AVLTree, AVLNode

def main():
    #node = AVLNode(10,3)
    #print(node)
    tree = AVLTree()
    print(tree.insert(6,0))
    print(tree.insert(7,1))
    print(tree.insert(8,2))
    #print(tree.avl_to_array())
    print("root:",tree.get_root())
    print("size:",tree.size())
    #print(tree.search(1))
    #a = tree.search(2)
    #tree.delete(a)
    #print(tree.size())
    #print(tree.avl_to_array())
    #print(tree.split(AVLNode(5,1)))
    print("end")

if __name__ == '__main__':
    main()
