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
		return str(self.key)+","+str(self.value)


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node): #(:
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""

	def set_right(self, node): #(:
		self.right = node
	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node): #(-:
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.get_key() is not None

	def set_sons_to_virtual(self):
		virtual_left = AVLNode(None, None)
		virtual_right = AVLNode(None, None)
		self.set_left(virtual_left)
		self.set_right(virtual_right)
		virtual_left.set_parent(self)
		virtual_right.set_parent(self)


	def BF(self): #Balance_Factor
		return self.get_left().get_height() - self.get_right().get_height()

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.size = 0
		#height
		# add your fields here



	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key): #recursive-solution
		x = self.get_root()
		if x is None or key == x.get_key():
			return x
		if key<x.get_key():
			return AVLTree.search(x.get_left(),key)
		else:
			return AVLTree.search(x.get_right(),key)


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val): #TODO don't forget to return the num of rotations + size updating, find where rebalancing is needed without rotation (field update)
		rebalancing = 0
		if self.root is None: #the tree is empty - so we insert the node as the root
			self.root = AVLNode(key,val)
			self.root.set_sons_to_virtual()
		else:
			z = AVLNode(key, val)
			y = self.Tree_position(key)
			prev_height = y.get_height() #??
			z.set_parent(y)
			if z.get_key() < y.get_key():
				y.set_left(z)
			else:
				y.set_right(z)
			z.set_sons_to_virtual()
			#__________
			while y.is_real_node():
				bf = y.BF()
				if bf<abs(2) and y.get_height() == prev_height:
					#update height?
					break
				elif bf<abs(2) and y.get_height() != prev_height:
					y = y.get_parent()
					#prev_height = y.get_height()
				else:
					rebalancing += self.perform_rotation(y)
					break

		self.size += 1
		return rebalancing


	def Tree_position(self, key):
		x = self.root
		y = None
		while x is not None:
			y = x
			if key == x.get_key():
				return x
			if key < x.get_key():
				x = x.get_left()
			else:
				x = x.get_right()
		return y


	def is_left_child(self, node):
		if node.get_parent().get_left().get_key() == node.get_key():
			flag = True
		else:
			flag = False
		return flag


	def Right_rotation(self,A,B):
		flag = self.is_left_child(B)
		B.set_left(A.get_right())
		B.get_left().set_parent(B)
		A.set_right(B)
		A.set_parent(B.parent)
		if flag:
			A.get_parent.set_left(A)
		else:
			A.get_parent.set_right(A)
		B.set_parent(A)
		return None


	def Left_rotation(self,A,B):
		flag = self.is_left_child(B)
		B.set_right(A.get_left())
		B.get_right.set_parent(B)
		A.set_left(B)
		A.set_parent(B.get_parent())
		if flag:
			A.get_parent().set_left(A)
		else:
			A.get_parent().set_right(A)
		B.set_parent(A)
		return None


	def perform_rotation(self, y):
		if y.BF == 2:
			if y.left.BF == -1:
				self.Left_rotation(y, y.get_left())
				self.Right_rotation(y, y.get_left())
				rebalancing = 2
			else:
				self.Right_rotation(y, y.get_left())
				rebalancing = 1
		else:
			if y.left.BF == 1:
				self.Right_rotation(y, y.get_right())
				self.Left_rotation(y, y.get_right())
				rebalancing = 2
			else:
				self.Left_rotation(y, y.get_right())
				rebalancing = 1
		return rebalancing


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, z): #TODO + don't forget to return the num of rotations + size updating
		rebalancing = 0
		if self.size == 1:
			self.root = None
		else:
			x = z.get_parent()
			prev_height = x.get_height()
			if z.height == 0:
				if z.get_parent().get_right().is_real_node and z.get_parent().get_left().is_real_node():
					if z.is_left_child():
						z.get_parent().set_left(None)
					else:
						z.get_parent().set_left(None)

				else:
					z.set_sons_to_virtual()
			elif z.right is None or z.left is None:
				if z.is_left_child:
					if z.get_left() is not None:
						z.get_left().set_parent(z.parent)
						z.get_parent().set_left(z.left)
					else:
						z.get_right().set_parent(z.parent)
						z.get_parent().set_left(z.right)
				else:
					if z.left is not None:
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
						y.get_parent().set_left(None)
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
				bf = x.BF
				if bf<abs(2) and x.get_height() == prev_height:
					break
				elif bf<abs(2) and x.get_height() != prev_height:
					x = x.get_parent()
				else:
					self.perform_rotation(x)
					x = x.get_parent()
		self.size -= 1
		return rebalancing



	def minimum(self, node):
		while node.get_left().is_real_node():
			node = node.get_left()
		return node


	def successor(self, x):
		if x.get_right().is_real_node():
			return self.minimum(x.right)
		y = x.get_parent()
		while y.is_real_node() and (x == y.get_right()):
			x = y
			y = x.get_parent()
		return y



	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of tuples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return self.list_Inorder([])

	#avl_to_array helper
	def list_Inorder(self, rlist):
		x = self.get_root()
		if x is None:
			return []
		x.get_left().list_Inorder(rlist)
		rlist.append((x.get_key(),x.get_value()))
		x.get_right().list_Inorder(rlist)
		return rlist


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.size	

	
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""

	def split(self, node):
		left_tree = AVLTree()  # left_tree<NODE
		right_tree = AVLTree()  # NODE<right_tree
		left_tree.root, right_tree.root = self.split_helper(self.root, node, left_tree,
															right_tree)  # setting the roots for each tree
		left_tree = left_tree.join(node.get_left(), left_tree.root.get_key(),
								   left_tree.root.get_value())  # join with the left son of splitkey (node)
		right_tree = node.get_right().join(right_tree, right_tree.root.get_key(),
									 right_tree.root.get_value())  # join with the right son of splitkey (node)
		return [left_tree, right_tree]

	def split_helper(self, node, splitkey, left_tree, right_tree):  # recursive helper function
		if not AVLNode.is_real_node(node):
			return None, None
		if node.key < splitkey:
			left_subtree, right_subtree = self.split_helper(node.get_right(), splitkey, left_tree, right_tree)
			left_tree = left_tree.join(right_subtree, node.get_key(), node.get_value())
			return node, right_subtree
		if node.key > splitkey:
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
				if c.BF == 2 or c.BF == -2:
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
				if c.BF == 2 or c.BF == -2:
					tree2.perform_rotation(c)

		return cost


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
