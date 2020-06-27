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

def return_kth_to_last(root,k):
    k = max(k-1,0)
    if root is None:
        return None
    head, tail = root, root
    while 0 < k:
        k -= 1
        if tail.next is None:
            return None
        tail = tail.next
    while tail.next is not None:
        tail = tail.next
        head = head.next
    return head

root = None
for i in range(20):
    root = insert(root, i)
root.print()

print(return_kth_to_last(root,-434).data)
