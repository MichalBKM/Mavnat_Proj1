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

	#print func - delete before submitting!!!
	#def __repr__(self):
		#return "<"+str(self.key)+","+str(self.value)+">"


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self): #DONT EDIT
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self): #DONT EDIT
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self): #DONT EDIT
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self): #DONT EDIT
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self): #DONT EDIT
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self): #DONT EDIT
		if not self.is_real_node():
			return -1
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node): #DONT EDIT
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""

	def set_right(self, node): #DONT EDIT
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node): #DONT EDIT
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key): #DONT EDIT
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value): #DONT EDIT
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h): #DONT EDIT
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self): #DONT EDIT
		return self.get_key() is not None

	def set_sons_to_virtual(self): #DONT EDIT
		virtual_left = AVLNode(None, None)
		virtual_right = AVLNode(None, None)
		self.set_left(virtual_left)
		self.set_right(virtual_right)
		virtual_left.set_parent(self)
		virtual_right.set_parent(self)

	#BF = Balance_Factor
	def BF(self): #DONT EDIT
		return self.left.get_height() - self.right.get_height()


	def update_height(self):
		if not self.is_real_node():
			self.height = -1
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
	def search(self,key):
		x = self.get_root()
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

	""" #before putting the rotations inside the func
	def insert(self, key, val):
		node = AVLNode(key, val)
		node.set_sons_to_virtual()
		y = self.Tree_position(key)
		node.set_parent(y)
		if y is None:
			self.root = node
		elif key< y.get_key():
			y.set_left(node)
		else:
			y.set_right(node)
		node.update_height()
		rebalancing = 0

		while y is not None: #and not y.is_real_node()
			new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())
			bf = y.BF()
			if abs(bf)<2 and y.get_height() == new_height: #3.2 IN ALGORITHM
				break
			elif abs(bf)<2 and y.get_height() != new_height: #3.3 IN ALGORITHM
				y.update_height()
				rebalancing += 1
			else: #abs(bf)==2 3.4 IN ALGORITHM
				rebalancing += self.perform_rotation(y)
				break
			y = y.get_parent()
		self.tree_size += 1
		return rebalancing
	"""


	def insert(self, key, val):
		node = AVLNode(key, val)
		node.set_sons_to_virtual()
		y = self.Tree_position(key)
		node.set_parent(y)
		if y is None:
			self.root = node
		elif key< y.get_key():
			y.set_left(node)
		else:
			y.set_right(node)
		node.update_height()
		rebalancing = 0

		while y is not None:
			new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())
			bf = y.BF()
			if abs(bf)<2 and y.get_height() == new_height: #3.2 IN ALGORITHM
				break
			elif abs(bf)<2 and y.get_height() != new_height: #3.3 IN ALGORITHM
				y.update_height()
				rebalancing += 1
			else: #abs(bf)==2 3.4 IN ALGORITHM
				rebalancing += self.perform_rotation(y) #break???
			y = y.get_parent()
		self.tree_size += 1
		return rebalancing



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


	def Right_rotation(self,B):
		is_root = False
		if B.get_key() == self.get_root().get_key():
			is_root = True #the criminal is the root
		A = B.get_left()
		B.set_left(A.get_right())
		B.get_left().set_parent(B)
		A.set_right(B)
		A.set_parent(B.get_parent())
		if A.get_parent() is not None:
			if B.get_parent().get_left().get_key() == B.get_key():
				A.get_parent().set_left(A)
			else:
				A.get_parent().set_right(A)
		B.set_parent(A)
		if is_root:
			self.root = A
		B.update_height()
		A.update_height()


	def Left_rotation(self,B):
		is_root = False
		if B.get_key() == self.get_root().get_key():
			is_root = True  #the criminal is the root
		A = B.get_right()
		B.set_right(A.get_left())
		B.get_right().set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent())
		if A.get_parent() is not None:
			if B.get_parent().get_left().get_key() == B.get_key():
				A.get_parent().set_left(A)
			else:
				A.get_parent().set_right(A)
		B.set_parent(A)
		if is_root:
			self.root = A
		B.update_height()
		A.update_height()



	def perform_rotation(self, y):
		if y.BF() == 2:
			if y.get_left().BF() == -1:
				self.Left_rotation(y.get_left())
				self.Right_rotation(y)
				rebalancing = 2
			else:  # +1 or 0 for delete , +1 only for insert
				self.Right_rotation(y)
				rebalancing = 1
		else:  # BF==-2
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

	def delete(self, node):
		rebalancing = 0
		virtual = AVLNode(None, None)
		y = None
		if self.get_root().get_key() == node.get_key():
			root = True
		else:
			root = False
		if not node.get_left().is_real_node() and not node.get_right().is_real_node(): #node is a leaf
			if root:
				self.root = None
			else:
				y = node.get_parent()
				if y.get_left().get_key() == node.get_key():
					y.set_left(virtual)
				else:
					y.set_right(virtual)
				virtual.set_parent(y)
		elif node.get_left().is_real_node() and not node.get_right().is_real_node(): #node has only left child
			if root:
				self.root = node.get_left()
				node.get_left().set_parent(None)
			else:
				y = node.get_parent()
				if y.get_left().get_key() == node.get_key():
					y.set_left(node.get_left())
				else:
					y.set_right(node.get_left())
				node.get_left().set_parent(y)
		elif not node.get_left().is_real_node() and node.get_right().is_real_node(): #node has only right child
			if root:
				self.root = node.get_right()
				node.get_right().set_parent(None)
			else:
				y = node.get_parent()
				if y.get_left().get_key() == node.get_key():
					y.set_left(node.get_right())
				else:
					y.set_right(node.get_right())
				node.get_right().set_parent(y)
		else: #node has two children
			successor = self.successor(node)
			if root:
				y = successor.get_parent()
				if self.get_root().get_key() == y.get_key():
					self.root = successor
					successor.set_left(y.get_left())
					successor.set_parent(None)
					y.get_left().set_parent(successor)
					y = self.get_root()
				else:
					y.set_left(successor.get_right())
					successor.get_right().set_parent(y)
					node.get_left().set_parent(successor)
					node.get_right().set_parent(successor)
					successor.set_left(node.get_left())
					successor.set_right(node.get_right())
					successor.set_parent(None)
					self.root = successor
			else:
				x = successor.get_parent()
				if x is node:
					node.get_left().set_parent(successor)
					successor.set_left(x.get_left())
					successor.set_parent(x.get_parent())
					if x.get_parent().get_left().get_key() == x.get_key():
						x.get_parent().set_left(successor)
					else:
						x.get_parent().set_right(successor)
					y = successor
				else:
					x.set_left(successor.get_right())
					successor.get_right().set_parent(x)
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
					y = x
		while y is not None:
			new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())
			bf = y.BF()
			if abs(bf) < 2 and y.get_height() == new_height:  # 3.2 IN ALGORITHM
				break
			elif abs(bf) < 2 and y.get_height() != new_height:  # 3.3 IN ALGORITHM
				y.update_height()
				rebalancing += 1
			else:  # abs(bf)==2 3.4 IN ALGORITHM
				rebalancing += self.perform_rotation(y)
				y = y.get_parent() #we added this because of UNITtest
			y = y.get_parent()
		self.tree_size -= 1
		return rebalancing



	def minimum(self): #WORKS WELL - DONT EDIT
		x = self.get_root()
		if x is None:
			return None
		while x.get_left().is_real_node():
			x = x.get_left()
		return x


	def successor(self, x): #WORKS WELL - DONT EDIT
		if not x.is_real_node():
			return None
		if x.get_right().is_real_node():
			z = x.get_right()
			while z.get_left().is_real_node():
				z = z.get_left()
			return z
		y = x.get_parent()
		while y is not None and x.get_key() == y.get_right().get_key():
			x = y
			y = y.get_parent()
		return y



	"""returns an array representing dictionary 
	@rtype: list
	@returns: a sorted list according to key of tuples (key, value) representing the data structure
	"""
	def avl_to_array(self): #WORKS WELL - DONT EDIT
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
	def size(self): #WORKS WELL
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

	def split(self, node): #update heights??
		t1 = AVLTree()
		t2 = AVLTree()
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
			if x is y.get_right():
				tmp1.root = y.get_left()
				y.get_left().set_parent(None)
				t1.join(tmp1, y.get_key(), y.get_value())
				tmp1.root = None
			else:
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
		if self.get_root().get_key() < key:
			small_tree = self
			big_tree = tree2
		else:
			small_tree = tree2
			big_tree = self
		h1 = small_tree.get_root().get_height()
		h2 = big_tree.get_root().get_height()

		if h1<=h2: #the small tree is also the shorter one
			a = small_tree.get_root()
			b = big_tree.get_root()
			while b.get_height() > a.get_height() :
				b = b.get_left()
			c = b.get_parent()
			d = c
			a.set_parent(x)
			x.set_left(a)
			b.set_parent(x)
			x.set_right(b)
			x.set_parent(c)
			x.update_height()
			if c is not None:
				c.set_left(x)
			while c is not None:
				bf = c.BF()
				if abs(bf) < 2:
					c.update_height()
				else: #abs(bf)==2
					big_tree.perform_rotation(c)
				c = c.get_parent()
			self.tree_size = small_tree.size() + big_tree.size() + 1
			if d is not None:
				self.root = big_tree.get_root()
			else:
				self.root = x

		else: #the small tree is the higher one
			a = big_tree.get_root()
			b = small_tree.get_root()
			while b.get_height() > a.get_height():
				b = b.get_right()
			c = b.get_parent()
			a.set_parent(x)
			x.set_left(a)
			b.set_parent(x)
			x.set_right(b)
			x.set_parent(c)
			x.update_height()
			if c is not None:
				c.set_right(x)
			while c is not None:
				bf = c.BF()
				if abs(bf) < 2:
					c.update_height()
				else:
					small_tree.perform_rotation(c)
				c = c.get_parent()
			self.root = small_tree.get_root()
			self.tree_size = small_tree.size() + big_tree.size() + 1


		return cost





	"""returns the root of the tree representing the dictionary
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self): #WORKS WELL
		return self.root
