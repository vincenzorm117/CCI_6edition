#!/usr/local/bin/python3

from random import randint

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def print(self):
        curr = self
        while curr is not None:
            print(curr.data,end=" ")
            curr = curr.next
        print()
    def count(self):
        count, curr = 0, self
        while curr is not None:
            count += 1
            curr = curr.next
        return count

def insert(root,data):
    if root is None:
        root = Node(data)
    else:
        curr = root
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(data)
    return root

def find(root,data):
    while root is not None:
        if root.data == data:
            return root
        root = root.next
    return None

def tail(root):
    if root is None:
        return None
    while root.next is not None:
        root = root.next
    return root



def palindrome(root):
    count = root.count()
    left = root
    for i in range(int(count/2)):
        right = left
        for j in range(count - 2*i - 1):
            right = right.next
        if right.data != left.data:
            return False
        left = left.next
    return True

root = None
x = list(range(10))
for i in x:
    root = insert(root, i)
print(palindrome(root))
root = insert(root, 6)
x.reverse()
for i in x:
    root = insert(root, i)


root.print()
print(palindrome(root))

