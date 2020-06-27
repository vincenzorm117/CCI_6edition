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

def delete_middle_node(target):
    if target is None:
        return None
    if target.next is None:
        del target
        return None
    target.data = target.next.data
    d = target.next
    target.next = target.next.next
    del d
    return target

root = None
for i in range(5):
    root = insert(root, i)
root = insert(root,5)
for i in range(6,11):
    root = insert(root, i)

root.print()
delete_middle_node(find(root,7))
root.print()


