#username1 - Berkheim1
#id1      - 207795154
#name1    - Michal Berkheim
#username2 - hilaperry
#id2      - 212648547
#name2    - Hila Perry

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	#time complexity: O(1)
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	#time complexity: O(1)
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	#time complexity: O(1)
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	#time complexity: O(1)
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	#time complexity: O(1)
	def get_value(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	#time complexity: O(1)
	def get_height(self):
		if not self.is_real_node():
			return -1
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)
	def set_left(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)
	def set_parent(self, node):
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	#time complexity: O(1)
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	#time complexity: O(1)
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	#time complexity: O(1)
	def set_height(self, h):
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	#time complexity: O(1)
	def is_real_node(self):
		return self.get_key() is not None

	"""sets left and right sons to virtual nodes
 	"""
	#time complexity: O(1)
	def set_sons_to_virtual(self):
		#creates virtual children
		virtual_left = AVLNode(None, None)
		virtual_right = AVLNode(None, None)
		#links node and virtual nodes
		self.set_left(virtual_left)
		self.set_right(virtual_right)
		virtual_left.set_parent(self)
		virtual_right.set_parent(self)

	"""returns the balance factor of the node

  	@rtype: int
   	@returns: the balance factor of the node
   	"""
	#time complexity: O(1)
	#BF = Balance_Factor
	def BF(self):
		return self.left.get_height() - self.right.get_height()

	"""updates the height of the node according to the heights of its children
 	"""
	#time complexity: O(1)
	def update_height(self):
		#if the node is virtual, its height should be -1
		if not self.is_real_node():
			self.height = -1
		#else, its height should be calculated according to the heights of its children
		else:
			self.height = 1 + max(self.left.height, self.right.height)






"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):


	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.tree_size = 0

	"""searches for a AVLNode in the dictionary corresponding to the key
	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	#time complexity: O(log n)
	def search(self,key):
		x = self.get_root()
		#comparing x's key to the input key until we traverse the tree and find x or return None if we don't
		while x is not None and x.is_real_node():
			if key == x.get_key():
				return x
			elif key < x.get_key():
				x = x.get_left()
			else:
				x = x.get_right()
		if not x.is_real_node():
			return None
		return x


	"""inserts val at position i in the dictionary
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	#time complexity: O(log n)
	def insert(self, key, val):
		node = AVLNode(key, val)
		node.set_sons_to_virtual()
		y = self.Tree_position(key) #finding the correct position for insertion of the node
		node.set_parent(y)
		if y is None: #self is an empty tree
			self.root = node
		#checking if the node should be a right or left child
		elif key< y.get_key():
			y.set_left(node)
		else:
			y.set_right(node)
		node.update_height()
		rebalancing = 0

		#restoring the shape of the tree as taught in class
		while y is not None:
			new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())
			bf = y.BF()
			if abs(bf)<2 and y.get_height() == new_height: #3.2 IN ALGORITHM
				break
			elif abs(bf)<2 and y.get_height() != new_height: #3.3 IN ALGORITHM
				y.update_height()
				rebalancing += 1
			else: #abs(bf)==2, 3.4 IN ALGORITHM
				rebalancing += self.perform_rotation(y)
			y = y.get_parent()
		self.tree_size += 1
		return rebalancing


	"""finds the correct position for insertion to the tree given a key

 	@type key: int
	@pre: key currently does not appear in the dictionary
	@param: key of item that is to be inserted to self
 	@rtype: int
 	@returns: the correct position for insertion to the tree
 	"""
	#time complexity: O(log n)
	def Tree_position(self, key):
		x = self.get_root()
		y = None
		while x is not None and x.is_real_node():
			y = x
			if key < x.get_key():
				x = x.get_left()
			else:
				x = x.get_right()
		return y


	"""performs a right rotation as taught in class in order to balance the tree

 	@type B: AVLNode
  	@param B: the node that we want to perform the rotation on
 	"""
	#time complexity: O(1)
	def Right_rotation(self,B):
		is_root = False
		if B.get_key() == self.get_root().get_key():
			is_root = True #the criminal is the root
		A = B.get_left()
		B.set_left(A.get_right())
		B.get_left().set_parent(B)
		A.set_right(B)
		A.set_parent(B.get_parent())
		if A.get_parent() is not None: #if B wasn't the root
			if B.get_parent().get_left().get_key() == B.get_key(): #if B was a left child
				A.get_parent().set_left(A)
			else: #if B was a right child
				A.get_parent().set_right(A)
		B.set_parent(A)
		if is_root:
			self.root = A
		B.update_height()
		A.update_height()


	"""performs a left rotation as taught in class in order to balance the tree

 	@type B: AVLNode
  	@param B: the node that we want to perform the rotation on
 	"""
	#time complexity: O(1)
	def Left_rotation(self,B):
		is_root = False
		if B.get_key() == self.get_root().get_key():
			is_root = True  #the criminal is the root
		A = B.get_right()
		B.set_right(A.get_left())
		B.get_right().set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent())
		if A.get_parent() is not None: #if B wasn't the root
			if B.get_parent().get_left().get_key() == B.get_key(): #if B was a left child
				A.get_parent().set_left(A)
			else: #if B was a right child
				A.get_parent().set_right(A)
		B.set_parent(A)
		if is_root:
			self.root = A
		B.update_height()
		A.update_height()



	"""performs a rotation according to the bf of y and it's son in order to balance the tree
	
 	@type y: AVLNode
  	@pre y: y has a balance factor of 2 or -2
  	@param y: the node that we want to perform the rotation on
   	@rtype: int
    	@returns: the number of rebalancing operations when performing the rotation
 	"""
	#time complexity: O(1)
	def perform_rotation(self, y):
		if y.BF() == 2:
			if y.get_left().BF() == -1:
				self.Left_rotation(y.get_left())
				self.Right_rotation(y)
				rebalancing = 2
			else:  # +1 or 0 for delete , +1 only for insert
				self.Right_rotation(y)
				rebalancing = 1
		else:  # BF == -2
			if y.get_right().BF() == 1:
				self.Right_rotation(y.get_right())
				self.Left_rotation(y)
				rebalancing = 2
			else:  # -1 or 0 for delete , -1 only for insert
				self.Left_rotation(y)
				rebalancing = 1
		return rebalancing





	"""deletes node from the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	#time complexity: O(log n)
	def delete(self, node): #finish documentation
		rebalancing = 0
		virtual = AVLNode(None, None)
		y = None
		if self.get_root().get_key() == node.get_key():
			root = True
		else:
			root = False
		if not node.get_left().is_real_node() and not node.get_right().is_real_node(): #node is a leaf
			if root: #tree contains only one node
				self.root = None
			else: #updating the child of node's parent
				y = node.get_parent()
				if y.get_left().get_key() == node.get_key(): #node is the left child of y
					y.set_left(virtual)
				else: #node is the right child of y
					y.set_right(virtual)
				virtual.set_parent(y)
		elif node.get_left().is_real_node() and not node.get_right().is_real_node(): #node has only left child
			if root: #self is AVL so it's only the root and its left child
				self.root = node.get_left() #left child becomes root
				node.get_left().set_parent(None)
			else: #bypassing the node by connecting it's parent to it's child
				y = node.get_parent()
				if y.get_left().get_key() == node.get_key(): #node is the left child of y
					y.set_left(node.get_left())
				else: #node is the left child of y
					y.set_right(node.get_left())
				node.get_left().set_parent(y)
		elif not node.get_left().is_real_node() and node.get_right().is_real_node(): #node has only right child
			if root: #self is AVL so it's only the root and its right child
				self.root = node.get_right() #right child becomes root
				node.get_right().set_parent(None)
			else: #bypassing the node by connecting it's parent to it's child
				y = node.get_parent()
				if y.get_left().get_key() == node.get_key(): #node is the left child of y
					y.set_left(node.get_right())
				else: #node is the right child of y
					y.set_right(node.get_right())
				node.get_right().set_parent(y)
		else: #node has two children
			successor = self.successor(node) #successor has no left child, because otherwise it's left child would have been the successor
			if root:
				y = successor.get_parent()
				if self.get_root().get_key() == y.get_key(): #the root has a right child which doesn't a left child
					#right child (successor) becomes the new root
					self.root = successor
					#left child of the old root becomes left child of the new root
					successor.set_left(y.get_left())
					successor.set_parent(None)
					y.get_left().set_parent(successor)
					y = self.get_root()
				else: #right child has a left child
					#right child of successor becomes left child of y
					y.set_left(successor.get_right())
					successor.get_right().set_parent(y)
					#successor becomes the new root
					node.get_left().set_parent(successor)
					node.get_right().set_parent(successor)
					successor.set_left(node.get_left())
					successor.set_right(node.get_right())
					successor.set_parent(None)
					self.root = successor
			else:
				x = successor.get_parent()
				#successor has no left child, because otherwise it's left child would have been the successor
				if x is node: #right child is the successor
					#left child of node becomes left child of the successor
					node.get_left().set_parent(successor)
					successor.set_left(x.get_left())
					#parent of node becomes the parent of the successor
					successor.set_parent(x.get_parent())
					if x.get_parent().get_left().get_key() == x.get_key():
						x.get_parent().set_left(successor)
					else:
						x.get_parent().set_right(successor)
					y = successor
				else:
					#right child of successor becomes left child of x
					x.set_left(successor.get_right())
					successor.get_right().set_parent(x)
					#replacing node with successor node
					node.get_left().set_parent(successor)
					node.get_right().set_parent(successor)
					successor.set_left(node.get_left())
					successor.set_right(node.get_right())
					y = node.get_parent()
					successor.set_parent(y)
					if y.get_left().get_key() == node.get_key():
						y.set_left(successor)
					else:
						y.set_right(successor)
					y = x #balancing should start from successor's old parent because it's the lowest node that we changed its children
		while y is not None:
			new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())
			bf = y.BF()
			if abs(bf) < 2 and y.get_height() == new_height:  # 3.2 IN ALGORITHM
				break
			elif abs(bf) < 2 and y.get_height() != new_height:  # 3.3 IN ALGORITHM
				y.update_height()
				rebalancing += 1
			else:  # abs(bf)==2, 3.4 IN ALGORITHM
				rebalancing += self.perform_rotation(y)
				y = y.get_parent()
			y = y.get_parent()
		self.tree_size -= 1
		return rebalancing


	"""returns the node with the minimal key

 	@rtype = AVLNode
  	@returns: the node with the minimal key or None if there are no elements in the dictionary
 	"""
	#time complexity: O(log n)
	def minimum(self):
		x = self.get_root()
		if x is None: #if tree is empty
			return None
		while x.get_left().is_real_node():
			x = x.get_left() #keep going left
		return x


	"""returns the successor of the given node

 	@type x: AVLNode
  	@param: the node whose successor is requested
   	@rtype: AVLNode
    	@returns: the successor of the node, None if the node has the maximal key or it's the only node in the tree
 	"""
	#time complexity: O(log n)
	def successor(self, x):
		if not x.is_real_node(): #x is virtual
			return None
		if x.get_right().is_real_node(): #x has a right child
			z = x.get_right()
			while z.get_left().is_real_node():
				z = z.get_left() #keep going left
			return z
		y = x.get_parent() #x doesn't have a right child
		while y is not None and x.get_key() == y.get_right().get_key(): #go up from x until the first right turn 
			x = y
			y = y.get_parent()
		return y



	"""returns an array representing dictionary 
	@rtype: list
	@returns: a sorted list according to key of tuples (key, value) representing the data structure
	"""
	#time complexity: O(n)
	def avl_to_array(self): #inserting the nodes to an array via inorder walk
		if self.get_root() is None:
			return []
		rlist = []
		x = self.minimum()
		while x is not None and x.is_real_node():
			rlist.append((x.get_key(),x.get_value()))
			x = self.successor(x)
		return rlist



	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	#time complexity: O(1)
	def size(self):
		return self.tree_size

	
	"""splits the dictionary at the i'th index
	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	#time complexity: O(log n)
	def split(self, node):
		t1 = AVLTree() #smaller keys
		t2 = AVLTree() #bigger keys
		#adding the subtree(s) of node to the respective tree(s) if exist
		if node.get_left().is_real_node(): #if the node has left children
			t1.root = node.get_left()
			node.get_left().set_parent(None)
		if node.get_right().is_real_node(): #if the node has right children
			t2.root = node.get_right()
			node.get_left().set_parent(None)
		y = node.get_parent()
		x = node
		tmp1 = AVLTree()
		tmp2 = AVLTree()
		while y is not None: #going up the tree
			if x is y.get_right(): #y's left subtree is smaller than x, thus should be added to t1
				tmp1.root = y.get_left()
				y.get_left().set_parent(None)
				t1.join(tmp1, y.get_key(), y.get_value())
				tmp1.root = None
			else: #y's right subtree is bigger than x, thus should be added to t2
				tmp2.root = y.get_right()
				y.get_right().set_parent(None)
				t2.join(tmp2, y.get_key(), y.get_value())
				tmp2.root = None
			x = y
			y = y.get_parent()
		return [t1, t2]



	"""joins self with key and another AVLTree
	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key seperating self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	#time complexity: O(log n)
	def join(self, tree2, key, val):
		if self.get_root() is None and tree2.get_root() is None: #both trees are empty
			self.insert(key,val)
			return 1

		#one of the trees are empty and the other not
		if self.get_root() is None: #self is empty
			orig_height = tree2.get_root().get_height()
			tree2.insert(key, val)
			self.root = tree2.root #self is becoming the new tree
			#print("size:", self.size())
			return orig_height + 2  # original height minus -1 (empty tree), plus 1 = height+2
		elif tree2.get_root() is None: #tree2 is empty
			orig_height = self.get_root().get_height()
			self.insert(key,val) #now self is the new tree
			#print("size:", self.size())
			return orig_height+2 #original height minus -1 (empty tree), plus 1 = height+2

		#joining two trees that are not empty
		cost = abs(self.get_root().get_height()-tree2.get_root().get_height()) + 1
		x = AVLNode(key, val) #x is the connecting node
		small_tree = AVLTree() #the tree with the smaller values - will be on the left side of the joined tree
		big_tree = AVLTree() #the tree with the bigger values - will be on the right side of the joined tree
		if self.get_root().get_key() < key: #self is the has the smaller keys
			small_tree = self
			big_tree = tree2
		else: #self has the bigger keys
			small_tree = tree2
			big_tree = self
		h1 = small_tree.get_root().get_height()
		h2 = big_tree.get_root().get_height()

		if h1<=h2: #the small tree is also the shorter one
			a = small_tree.get_root()
			b = big_tree.get_root()
			while b.get_height() > a.get_height() : #finding the first vertex on the left spine of t2 with height <=h
				b = b.get_left()
			#attaching x to b's former parent
			c = b.get_parent()
			d = c
			a.set_parent(x)
			x.set_left(a)
			b.set_parent(x)
			x.set_right(b)
			x.set_parent(c)
			x.update_height()
			if c is not None: #if b is not the root
				c.set_left(x)
			while c is not None: #rebalancing
				bf = c.BF()
				if abs(bf) < 2:
					c.update_height()
				else: #abs(bf)==2
					big_tree.perform_rotation(c)
				c = c.get_parent()
			self.tree_size = small_tree.size() + big_tree.size() + 1
			if d is not None: #if b wasn't the root
				self.root = big_tree.get_root()
			else: #if b was the root
				self.root = x

		else: #the small tree is the higher one
			a = big_tree.get_root()
			b = small_tree.get_root()
			while b.get_height() > a.get_height(): #finding the first vertex on the left spine of t2 with height <=h
				b = b.get_right()
			#attaching x to b's former parent
			c = b.get_parent()
			d = c
			a.set_parent(x)
			x.set_left(a)
			b.set_parent(x)
			x.set_right(b)
			x.set_parent(c)
			x.update_height()
			if c is not None: #if b is not the root
				c.set_right(x)
			while c is not None: #rebalancing
				bf = c.BF()
				if abs(bf) < 2:
					c.update_height()
				else: #abs(bf)==2
					small_tree.perform_rotation(c)
				c = c.get_parent()
			self.tree_size = small_tree.size() + big_tree.size() + 1
			if d is not None: #if b wasn't the root
				self.root = small_tree.get_root()
			else: #if b was the root
				self.root = x

		return cost



	"""returns the root of the tree representing the dictionary
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	#time complexity: O(1)
	def get_root(self):
		return self.root


