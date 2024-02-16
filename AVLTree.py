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
	def __repr__(self):
		return "<"+str(self.key)+","+str(self.value)+">"


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
		return self.get_left().get_height() - self.get_right().get_height()

	def is_left_child(self):
		if self.get_parent().get_left().get_key() == self.get_key():
			flag = True
		else:
			flag = False
		return flag

	def update_height(self):
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

	#TODO
	def insert(self, key, val): #don't forget to return the num of rotations + size updating, find where rebalancing is needed without rotation (field update)
		rebalancing = 0
		z = AVLNode(key,val)
		z.set_sons_to_virtual()
		if self.root is None: #the tree is empty - so we insert the node as the root
			self.root = z
			z.update_height()
		else:
			y = self.Tree_position(key)
			z.set_parent(y) #y is the father of z
			if z.get_key() < y.get_key():
				y.set_left(z)
			elif z.get_key() > y.get_key() :
				y.set_right(z)
			z.update_height()
			"""
			while y is not None and y.is_real_node():
				bf = y.BF()
				new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())
				if abs(bf)<2 and y.get_height() == new_height: #3.2 in algorithm
					break
				elif abs(bf)<2 and y.get_height() != new_height: #3.3 in algorithm
					y.update_height()
					rebalancing += 1
					y = y.get_parent()
				else: #3.4 in algorithm
					rebalancing += self.perform_rotation(y)
					break
				"""
		self.tree_size += 1
		return rebalancing

	"""
	#ROTATIONS NEED TO BE FIXED!
	def insert(self, key, val): #don't forget to return the num of rotations + size updating, find where rebalancing is needed without rotation (field update)
		rebalancing = 0
		z = AVLNode(key,val)
		z.set_sons_to_virtual()
		y = self.Tree_position(key)
		z.set_parent(y)  # y is the father of z
		#print("tree position: ", y)
		if y is None: #tree is empty - place z as the root
			self.root = z
			#print("root is", z)
		elif key < y.get_key(): #z is the left son of y
			y.set_left(z)
			#print("left son of ",y, " is ",z)
		else: #z.get_key() > y.get_key() - z is the right son of y
			y.set_right(z)
			#print("right son of ", y, " is ", z)
		#print("parent of ", z, " is ", y)
		z.update_height()

		#balancing + update heights
		while y is not None:
			bf = y.BF()
			new_height = 1 + max(y.get_left().get_height(), y.get_right().get_height())

			if abs(bf)<2 and y.get_height() == new_height: #3.2 in algorithm
				break

			elif abs(bf)<2 and y.get_height() != new_height: #3.3 in algorithm
				y.update_height()
				rebalancing += 1
				y = y.get_parent()

			else: #3.4 in algorithm - abs(bf)==2
				rebalancing += self.perform_rotation(y)
				break

		self.tree_size += 1
		return rebalancing
		"""

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


	def Right_rotation(self,A,B):
		flag = B.is_left_child()
		B.set_left(A.get_right())
		B.get_left().set_parent(B)
		A.set_right(B)
		A.set_parent(B.parent)
		if flag:
			A.get_parent().set_left(A)
		else:
			A.get_parent().set_right(A)
		B.set_parent(A)
		return None


	def Left_rotation(self,A,B):
		flag = B.is_left_child()
		B.set_right(A.get_left())
		B.get_right().set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent())
		if flag:
			A.get_parent().set_left(A)
		else:
			A.get_parent().set_right(A)
		B.set_parent(A)
		return None


	def perform_rotation(self, y):
		if y.BF() == 2:
			if y.get_left().BF() == -1:
				self.Left_rotation(y, y.get_left())
				self.Right_rotation(y, y.get_left())
				rebalancing = 2
			else: #+1 or 0 for delete , +1 only for insert
				self.Right_rotation(y, y.get_left())
				rebalancing = 1
		else: #BF==-2
			if y.get_left().BF() == 1:
				self.Right_rotation(y, y.get_right())
				self.Left_rotation(y, y.get_right())
				rebalancing = 2
			else: #-1 or 0 for delete , -1 only for insert
				self.Left_rotation(y, y.get_right())
				rebalancing = 1
		return rebalancing


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	#TODO
	def delete(self, z): #don't forget to return the num of rotations + size updating
		rebalancing = 0
		virtual = AVLNode(None, None)
		if self.tree_size == 1: #z is the root - so we delete it and now the tree is empty
			self.root = None
		else:
			x = z.get_parent()
			prev_height = x.get_height()
			if z.get_height() == 0:  #z is a leaf
				if z.get_parent().get_right().is_real_node() and z.get_parent().get_left().is_real_node():
					if z.is_left_child():
						z.get_parent().set_left(virtual)
					else:
						z.get_parent().set_right(virtual)
				else:
					z.set_sons_to_virtual()
			elif z.get_right() is None or z.get_left() is None:
				if z.is_left_child():
					if z.get_left() is not None:
						z.get_left().set_parent(z.parent)
						z.get_parent().set_left(z.left)
					else:
						z.get_right().set_parent(z.parent)
						z.get_parent().set_left(z.right)
				else:
					if z.get_left() is not None:
						z.get_left().set_parent(z.parent)
						z.get_parent().set_right(z.left)
					else:
						z.get_right().set_parent(z.parent)
						z.get_parent().set_right(z.right)
			else:
				y = self.successor(z)
				if y.get_right() is None:
					if not y.get_parent().get_right().is_real_node():
						y.get_parent().set_sons_to_virtual()
					else:
						y.get_parent().set_left(virtual)
				else:
					y.get_right().set_parent(y.get_parent)
					y.get_parent().set_left(y.get_right)
					z.get_left().set_parent(y)
					z.get_right().set_parent(y)
					if z.is_left_child():
						z.get_parent().set_left(y)
					else:
						z.get_parent().set_right(y)
			while x is not None:
				bf = x.BF()
				if bf<abs(2) and x.get_height() == prev_height:
					break
				elif bf<abs(2) and x.get_height() != prev_height:
					x = x.get_parent()
				else:
					self.perform_rotation(x)
					x = x.get_parent()
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
		print("rlist: ", rlist)
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
	#NEED TO RE-WRITE
	def split(self, node):
		left_tree = AVLTree()  # left_tree<NODE
		right_tree = AVLTree()  # NODE<right_tree
		splitkey = node.get_key()
		left_tree.root, right_tree.root = self.split_helper(self.get_root(), splitkey, left_tree, right_tree)  # setting the roots for each tree
		left_tree = left_tree.join(node.get_left(), left_tree.get_root().get_key(), left_tree.get_root().get_value())  # join with the left son of splitkey (node)
		right_tree = node.get_right().join(right_tree, right_tree.get_root().get_key(),right_tree.get_root().get_value())  # join with the right son of splitkey (node)
		return [left_tree, right_tree]

	def split_helper(self, node, splitkey, left_tree, right_tree):  # recursive helper function
		if not node.is_real_node():
			return None, None
		if node.get_key() < splitkey:
			left_subtree, right_subtree = self.split_helper(node.get_right(), splitkey, left_tree, right_tree)
			left_tree = left_tree.join(right_subtree, node.get_key(), node.get_value())
			return node, right_subtree
		if node.get_key() > splitkey:
			left_subtree, right_subtree = self.split_helper(node.get_left(), splitkey, left_tree, right_tree)
			right_tree = left_subtree.join(right_tree, node.get_key(), node.get_value())
			return left_subtree, node




	
	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val): #hila
		cost = abs(self.root.get_height() - tree2.root.get_height()) + 1
		tree1 = self
		x = AVLNode(key, val)
		if tree2 < x:
			tmp = tree2
			tree2 = tree1
			tree1 = tmp
			if tree1.root.get_height() < tree2.root.get_height():
				a = tree1.root
				b = tree2.root
				while b.get_height() > tree1.root.get_height():
					b = b.get_left()
				c = b.get_parent()
				a.set_parent(x)
				x.set_left(a)
				b.set_parent(x)
				x.set_right(b)
				x.set_parent(c)
				c.set_left(x)
				if c.BF() == 2 or c.BF() == -2:
					tree2.perform_rotation(c)
			else:
				a = tree2.root
				b = tree1.root
				while b.get_height() > tree2.root.get_height():
					b = b.get_right()
				c = b.get_parent()
				a.set_parent(x)
				x.set_right(a)
				b.set_parent(x)
				x.set_left(b)
				x.set_parent(c)
				c.set_right(x)
				if c.BF() == 2 or c.BF() == -2:
					tree2.perform_rotation(c)

		return cost


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self): #WORKS WELL
		return self.root
