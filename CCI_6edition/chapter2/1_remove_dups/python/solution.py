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

def remove_duplicates(root):
    buff = set()
    curr = root
    buff.add(curr.data)
    while curr is not None and curr.next is not None:
        if curr.next.data in buff:
            ndel = curr.next
            curr.next = curr.next.next
            del ndel
        else:
            curr = curr.next
            buff.add(curr.data)
    return root


def remove_duplicates_without_buffer(root):
    curr = root
    while curr is not None and curr.next is not None:
        lookahead = curr
        while lookahead.next is not None:
            if lookahead.next.data == curr.data:
                ndel = lookahead.next
                lookahead.next = lookahead.next.next
                del ndel
            else:
                lookahead = lookahead.next
        curr = curr.next
    return root

root = None
for i in range(13):
    root = insert(root, randint(0,9))
root.print()

remove_duplicates_without_buffer(root).print()
remove_duplicates(root).print()
