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
		self.size = 1
		

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
	def set_left(self, node):
		self.left = node
		node.parent = self
		self.height = 1 + max(self.left.height,self.right.height)
		node.height = self.height - 1
		return None


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node
		node.parent = self
		self.height = 1 + max(self.left.height,self.right.height)
		node.height = self.height - 1
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node
		if node.key > self.key:
			node.left = self
		else:
			node.right = self
		node.height = 1 + max(node.left.height,node.right.height)
		self.height = node.height - 1
		return None


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key
		return None


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value
		return None


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h
		return None


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return True if self.key!=None else False

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
		x = self.root
		if x==None or key==x.key:
			return x
		if key<x.key:
			return AVLTree.search(x.left,key)
		else:
			return AVLTree.search(x.right,key)


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
		if self.root==None:
			self.root = AVLNode(key,val)
			AVLNode.set_left(self.root, AVLNode(None, None))
			AVLNode.set_right(self.root,AVLNode(None,None))
		else:
			z = AVLNode(self, key, val)
			self.root.Tree_insert(z)
			y = z.parent
			while y.is_real_node:
				bf = self.BF(y)
				if -2<bf<2 and y.height == 1:
					return rebalancing
				elif -2<bf<2 and y.height == 0:
					y = y.parent
				else:
					if bf == 2:
						if self.BF(y.left) == 1:
							self.Right_rotation(self, y, y.left)
							rebalancing += 1
						else:
							self.Left_rotation(self, y, y.left)
							self.Right_rotation(self, y, y.left)
							rebalancing += 2
					else:
						if self.BF(y.left) == -1:
							self.Left_rotation(self, y, y.right)
							rebalancing += 1
						else:
							self.Right_rotation(self, y, y.right)
							self.Left_rotation(self, y, y.right)
							rebalancing += 2
			return rebalancing


	@staticmethod
	def BF(node): #Balance_Factor
		return node.left.height - node.right.height

	def Tree_position(self, key):
		x = self.root
		y = None
		while x!=None:
			y = x
		if key==x.key:
			return x
		if key < x.key:
			x = x.left
		else:
			x = x.right
		return y

	def Tree_insert(self,node):
		x = self.root
		z = node
		y = self.Tree_position(z.key)
		z.parent = y
		if z.key < y.key:
			y.left = z
		else:
			y.right = z

	def is_left_child(self, node):
		if node.parent.left.key == node.key:
			flag = True
		else:
			flag = False
		return flag

	def is_right_child(self, node):
		if node.parent.right.key == node.key:
			flag = True
		else:
			flag = False
		return flag


	def Right_rotation(self,A,B): #TODO update height and size
		flag = self.is_left_child(B)
		B.left = A.right
		B.left.parent = B
		A.right = B
		A.parent = B.parent
		if flag:
			A.parent.left = A
		else:
			A.parent.right = A
		B.parent = A


	def Left_rotation(self,A,B): #TODO update height and size
		flag = self.is_left_child(B)
		B.right = A.left
		B.right.parent = B
		A.left = B
		A.parent = B.parent
		if flag:
			A.parent.left = A
		else:
			A.parent.right = A
		B.parent = A


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, z): #TODO + don't forget to return the num of rotations + size updating
		if self.size == 1:
			self.root = None
		else:
			if z.height == 0:
				if self.is_left_child(self, z):
					virtual = AVLNode(None)
					



	@staticmethod
	def minimum(node):
		while node.left.is_real_node:
			node = node.left
		return node


	def successor(self, x):
		if x.right.is_real_node:
			return self.minimum(x.right)
		y = x.parent
		while y.is_real_node and (x == y.right):
			x = y
			y = x.parent
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
		if x==None:
			return []
		x.left.store_Inorder(rlist)
		rlist.append((x.key,x.value))
		x.right.store_Inorder(rlist)
		return rlist


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self): #TODO - because now we don't have size attribute in the tree
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
	def split(self, node): #T1<Node<T2
		T1 = AVLTree()
		T2 = AVLTree()
		#joining subtrees to create T1
		succ = self.successor(node)
		x = node
		while (x.key<succ.key):
			tmp1 = x.parent.left.join(x.parent, x.left)
			x = tmp1
		if (self.is_right_child(succ)):
			T1 = succ.parent.left.join(succ.parent, x)
		else:
			#TODO



	def is_root_of_subtree(self,node):
		if self.get_root()==node:
			return True
		return False
	
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
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
