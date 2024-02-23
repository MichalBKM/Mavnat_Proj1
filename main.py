from AVLTree import AVLTree, AVLNode

def main():

    b = AVLTree()
    b.insert(7,0)
    b.insert(6,1)
    b.insert(8,2)
    s = AVLTree()
    s.insert(2,10)
    s.insert(1,11)
    s.insert(3,12)

    #print(b.join(s,5,9))
    #print(b.avl_to_array())
    a = s.search(2)
    print("delete", s.delete(a))
    print(s.avl_to_array())
    print(s.get_root().get_left())



if __name__ == '__main__':
    main()
