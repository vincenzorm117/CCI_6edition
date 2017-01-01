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

def partition(root,pivot):
    curr = root
    l1 = l2 = r1 = r2 = None
    while curr is not None:
        n = curr.next
        if curr.data < pivot.data:
            if l1 is None:
                l1 = l2 = curr
            else:
                l2.next = curr
                l2 = l2.next
            l2.next = None
        else:
            if r1 is None:
                r1 = r2 = curr
            else:
                r2.next = curr
                r2 = r2.next
            r2.next = None
        curr = n
    l2.next = r1
    return l1


root = None
for i in range(10):
    root = insert(root, randint(0,9))
root = insert(root, 7)
for i in range(10):
    root = insert(root, randint(0,9))

root.print()
partition(root, find(root,7)).print()



