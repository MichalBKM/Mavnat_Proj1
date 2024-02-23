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

    print("join", b.join(s,5,9))
    print("root",b.get_root())
    print("to array",b.avl_to_array())
    print("search")
    a = b.search(2)
    print(a)
    print("delete", b.delete(a))
    print(b.get_root().get_left().get_right())
    #print("to array - after delete",b.avl_to_array())




if __name__ == '__main__':
    main()
