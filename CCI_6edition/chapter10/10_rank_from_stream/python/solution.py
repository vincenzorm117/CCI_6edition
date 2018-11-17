#!/usr/local/bin/python3



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
        


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self.root.insert(data)

    def print(self, root):
        if root is None:
            return
        print(root.data)
        self.print(root.left)
        self.print(root.right)
    
    def getRank(self, data):
        stack = []
        
        if self.root is None:
            return None
        if data == self.root.data:
            return 0 if self.root.left is None else self.root.left.size - 1

        curr = self.root
        while curr is not None and curr.data != data:
            if data <= curr.data:
                curr = curr.left
            else:
                leftValue = curr.left.size if curr.left is not None else 0
                stack.append(leftValue + 1)
                curr = curr.right
        sum = 0
        for s in stack:
            sum += s
        return sum
    


testcases = [
    [5,1,4,4,5,9,7,13,3]
]

for t in testcases:
    print(t)
    tree = BST()
    for value in t:
        tree.insert(value)

    for value in t:
        print(value, ':', tree.getRank(value))
