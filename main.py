from AVLTree import AVLTree, AVLNode

def main():
    #node = AVLNode(10,3)
    #print(node)
    tree = AVLTree()
    #tree.insert(6,0)
    #tree.insert(7,1)
    #tree.insert(8,2)
    tree.insert(8,0)
    tree.insert(7,1)
    tree.insert(6,2)
    #tree.Left_rotation()
    #print(tree.avl_to_array())
    #print("root:",tree.get_root())
    #print("size:",tree.size())
    #print(tree.size())
    #print(tree.avl_to_array())
    #print(tree.split(AVLNode(5,1)))
    print("end")

if __name__ == '__main__':
    main()
