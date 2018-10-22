#!/usr/local/bin/python3


class BST:
    class LLNode:
        def __init__(self, node):
            self.node = node
            self.prev = None
            self.next = None

	class Node:
		def __init__(self, data):
			self.data = data
			self.left = None
            self.right = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None
        self.head = None
        self.tail = None

	def insert(self, data):
		if self.root is None:
			self.root = self.Node(data)
            self.head = LLNode(self.root)
            self.tail = self.head
			return
		curr = self.root
		while curr is not None:
            if data <= curr.data:
                if curr.left is None:
                    curr.left = self.Node(data)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = self.Node(data)
                    break
                else:
                    curr = curr.right
    
    def find(self, data):
        curr = self.root
        while curr is not None and curr.data !- data:
            curr = curr.left if data <= curr.data else curr.right
        return curr

    def isLeaf(self, node):
        if node is None:
            raise Exception('Invalid node')
        return node.left == None and node.right == None

    def empty(self):
        return self.root == None

    def print(self):
        if self.root is None:
            print()
            return
        queue = [self.root]
        while 0 < len(queue):
            node = queue.pop(0)
            print(c)
            if c.left is not None:
                queue.append(node.left)
            if c.right is not None:
                queue.append(node.right)

    def parent(self, node):
        if node is None or not isinstance(node, self.Node) or self.root == node:
            return None
        curr = self.root
        while curr is not None:
            if curr.left == node or curr.right == node:
                return curr
            curr = curr.left if data <= curr.data else curr.right
        return None

    def findSubtreeMinNode(self, node):
        if node is None:
            raise Exception('Invalid argument')
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def findSubtreeMaxNode(self, node):
        if node is None:
            raise Exception('Invalid argument')
        curr = node
        while curr.right is not None:
            curr = curr.right
        return curr

    
    def delete(self, node):
        if node is None:
            raise Exception('Invalid argument')
        
        if node == self.root:
            if node.left is None:
                if node.right is None:
                    self.root = None
                else:
                    self.root = node.right
                del node
            else:
                if node.right is None:
                    self.root = node.left
                    del node
                else:
                    rightSubtreeMinNode = findSubtreeMinNode(node.right)
                    temp = rightSubtreeMinNode.data
                    rightSubtreeMinNode.data = self.root.data
                    self.root.data = temp
                    self.delete(rightSubtreeMinNode)
        else:
            parentNode = self.parent(node)
            if node.left is None:
                if node.right is None:
                    if parentNode.left == node:
                        parentNode.left = None
                    else:
                        parentNode.right = None
                else:
                    if parentNode.left == node:
                        parentNode.left = node.right
                    else:
                        parentNode.right = node.right
                del node
            else:
                if node.right is None:
                    if parentNode.left == node:
                        parentNode.left = node.left
                    else:
                        parentNode.right = node.left
                    del node
                else:
                    rightSubtreeMinNode = findSubtreeMinNode(node.right)
                    temp = rightSubtreeMinNode.data
                    rightSubtreeMinNode.data = self.root.data
                    self.root.data = temp
                    self.delete(rightSubtreeMinNode)

        


class BST_RAND():
	class Node:
		def __init__(self, data):
			self.data = data
			self.children = [None,None]
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None
		self.height = 0
		self.nodes = []

	def insert(self, data):
	def find(self, data):
	def empty(self):
	def print(self):
	def getRandomNode():










# class BST:
# 	class Node:
# 		def __init__(self, data):
# 			self.data = data
# 			self.left = None
#             self.right = None
# 		def __str__(self):
# 			return str(self.data)

# 	def __init__(self):
# 		self.root = None

# 	def insert(self, data):
# 		if self.root is None:
# 			self.root = self.Node(data)
# 			return
# 		curr = self.root
# 		while curr is not None:
#             if data <= curr.data:
#                 if curr.left is None:
#                     curr.left = self.Node(data)
#                     break
#                 else:
#                     curr = curr.left
#             else:
#                 if curr.right is None:
#                     curr.right = self.Node(data)
#                     break
#                 else:
#                     curr = curr.right
    
#     def find(self, data):
#         curr = self.root
#         while curr is not None and curr.data !- data:
#             curr = curr.left if data <= curr.data else curr.right
#         return curr

#     def isLeaf(self, node):
#         if node is None:
#             raise Exception('Invalid node')
#         return node.left == None and node.right == None

#     def empty(self):
#         return self.root == None

#     def print(self):
#         if self.root is None:
#             print()
#             return
#         queue = [self.root]
#         while 0 < len(queue):
#             node = queue.pop(0)
#             print(c)
#             if c.left is not None:
#                 queue.append(node.left)
#             if c.right is not None:
#                 queue.append(node.right)

#     def parent(self, node):
#         if node is None or not isinstance(node, self.Node) or self.root == node:
#             return None
#         curr = self.root
#         while curr is not None:
#             if curr.left == node or curr.right == node:
#                 return curr
#             curr = curr.left if data <= curr.data else curr.right
#         return None

#     def findSubtreeMinNode(self, node):
#         if node is None:
#             raise Exception('Invalid argument')
#         curr = node
#         while curr.left is not None:
#             curr = curr.left
#         return curr

#     def findSubtreeMaxNode(self, node):
#         if node is None:
#             raise Exception('Invalid argument')
#         curr = node
#         while curr.right is not None:
#             curr = curr.right
#         return curr

    
#     def delete(self, node):
#         if node is None:
#             raise Exception('Invalid argument')
        
#         if node == self.root:
#             if node.left is None:
#                 if node.right is None:
#                     self.root = None
#                 else:
#                     self.root = node.right
#                 del node
#             else:
#                 if node.right is None:
#                     self.root = node.left
#                     del node
#                 else:
#                     rightSubtreeMinNode = findSubtreeMinNode(node.right)
#                     temp = rightSubtreeMinNode.data
#                     rightSubtreeMinNode.data = self.root.data
#                     self.root.data = temp
#                     self.delete(rightSubtreeMinNode)
#         else:
#             parentNode = self.parent(node)
#             if node.left is None:
#                 if node.right is None:
#                     if parentNode.left == node:
#                         parentNode.left = None
#                     else:
#                         parentNode.right = None
#                 else:
#                     if parentNode.left == node:
#                         parentNode.left = node.right
#                     else:
#                         parentNode.right = node.right
#                 del node
#             else:
#                 if node.right is None:
#                     if parentNode.left == node:
#                         parentNode.left = node.left
#                     else:
#                         parentNode.right = node.left
#                     del node
#                 else:
#                     rightSubtreeMinNode = findSubtreeMinNode(node.right)
#                     temp = rightSubtreeMinNode.data
#                     rightSubtreeMinNode.data = self.root.data
#                     self.root.data = temp
#                     self.delete(rightSubtreeMinNode)

        