#!/usr/local/bin/python3

from random import randint


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self.root.insert(data)
    
    def find(data):
        if self.root is None:
            return None
        else:
            return self.root.find(data)
    
    def getRandomNode(self):
        # If no tree return None
        if self.root is None:
            return None
        # Else return random node
        index = randint(0, self.root.size - 1)
        return self.root.getIndexNode(index)
        
    

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, data):
        curr = self
        while True:
            curr.size += 1
            if data <= curr.data:
                if curr.left is None:
                    curr.left = BSTNode(data)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BSTNode(data)
                    break
                else:
                    curr = curr.right
    
    def find(self, data):
        curr = self
        while curr is not None and curr.data != data:
            curr = curr.left if data <= curr.data else curr.right
        return curr

    def getIndexNode(self, index):
        leftSize = 0 if self.left is None else self.left.size
        if index < leftSize:
            return self.left.getIndexNode(index)
        elif index == leftSize:
            return self
        else:
            return self.right.getIndexNode(index - (leftSize + 1))
        
        

# class BST:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.left = None
#             self.right = None
#             self.prev = None
#             self.next = None
#         def __str__(self):
#             return str(self.data)

#     def __init__(self):
#         self.root = None
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def LLAdd(self,node):
#         self.length += 1
#         self.tail.next = node
#         node.prev = self.tail
#         self.tail = node
    
#     def LLRemove(self, node):
#         self.length -= 1
#         if node.prev is None:
#             if node.next is None:
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.head = node.next
#                 self.head.prev = None
#         else:
#             if node.next is None:
#                 self.tail = node.prev
#                 self.tail.next = None
#             else:
#                 node.prev.next = node.next
#                 node.next.prev = node.prev

#     def insert(self, data):
#         if self.root is None:
#             self.root = self.Node(data)
#             self.head = self.root
#             self.tail = self.head
#             return
#         curr = self.root
#         while curr is not None:
#             if data <= curr.data:
#                 if curr.left is None:
#                     curr.left = self.Node(data)
#                     self.LLAdd(curr.left)
#                     break
#                 else:
#                     curr = curr.left
#             else:
#                 if curr.right is None:
#                     curr.right = self.Node(data)
#                     self.LLAdd(curr.right)
#                     break
#                 else:
#                     curr = curr.right
    
#     def find(self, data):
#         curr = self.root
#         while curr is not None and curr.data != data:
#             curr = curr.left if data <= curr.data else curr.right
#         return curr

#     def empty(self):
#         return self.root == None

#     def print2(self):
#         if self.root is None:
#             print()
#             return
#         curr = self.head
#         while curr is not None:
#             print(curr)
#             curr = curr.next

#     def print(self):
#         if self.root is None:
#             print()
#             return
#         queue = [self.root]
#         while 0 < len(queue):
#             node = queue.pop(0)
#             print(node)
#             if node.left is not None:
#                 queue.append(node.left)
#             if node.right is not None:
#                 queue.append(node.right)


#     def parent(self, node):
#         if node is None or not isinstance(node, self.Node) or self.root == node:
#             return None
#         curr = self.root
#         while curr is not None:
#             if curr.left == node or curr.right == node:
#                 return curr
#             curr = curr.left if node.data <= curr.data else curr.right
#         return None

#     def getRandomNode(self):
#         index = randint(0, self.length-1)
#         curr = self.head
#         while index >= 0:
#             curr = curr.next
#             index -= 1
#         return curr

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
#                 self.LLRemove(node)
#                 del node
#             else:
#                 if node.right is None:
#                     self.root = node.left
#                     self.LLRemove(node)
#                     del node
#                 else:
#                     rightSubtreeMinNode = self.findSubtreeMinNode(node.right)
#                     temp = rightSubtreeMinNode.data
#                     rightSubtreeMinNode.data = self.root.data
#                     self.root.data = temp
#                     print()
#                     self.print()
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
#                 self.LLRemove(node)
#                 del node
#             else:
#                 if node.right is None:
#                     if parentNode.left == node:
#                         parentNode.left = node.left
#                     else:
#                         parentNode.right = node.left
#                     self.LLRemove(node)
#                     del node
#                 else:
#                     rightSubtreeMinNode = self.findSubtreeMinNode(node.right)
#                     temp = rightSubtreeMinNode.data
#                     rightSubtreeMinNode.data = node.data
#                     node.data = temp
#                     self.delete(rightSubtreeMinNode)

        
# def checkFairness(bst):
#     if bst.empty():
#         return None
#     freq = {}
#     for _ in range(1000):
#         num = bst.getRandomNode().data
#         if num not in freq:
#             freq[num] = 0
#         freq[num] += 1
#     return freq

# # Create tree
# b = BST()
# b.insert(50)
# b.insert(60)
# b.insert(55)
# b.insert(65)
# b.insert(20)
# b.insert(40)
# b.insert(30)


# # b.print()
# # b.print2()
# print(checkFairness(b))

# b.insert(57)
# print(checkFairness(b))

# b.delete(b.find(60))
# print(checkFairness(b))

# b.delete(b.find(40))
# print(checkFairness(b))

# b.delete(b.find(30))
# print(checkFairness(b))

# b.print()

# b.delete(b.root)
# print(checkFairness(b))

# b.delete(b.root)
# print(checkFairness(b))
