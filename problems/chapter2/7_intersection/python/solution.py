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



def intersectionNSquared(r1,r2):
    c1 = r1
    while c1 is not None:
        c2 = r2
        while c2 is not None:
            if c1 == c2:
                return c1
            c2 = c2.next
        c1 = c1.next
    return None

def intersection(r1,r2):
    curr = [r1,r2]
    l = longer = None
    while curr[0] is not None and curr[1] is not None:
        curr[0] = curr[0].next
        curr[1] = curr[1].next

    if curr[0] is None and curr[1] is None:
        count = 0;
    else:
        l = curr[0] if curr[1] is None else curr[1]
        longer = 0 if curr[1] is None else 1
        count = 0
        while l is not None:
            count += 1
            l = l.next
    curr = [r1,r2]
    if l is not None:
        while 0 < count:
            curr[l] = curr.next
            curr -= 1
    while curr[0] != curr[1]:
        curr[0] = curr[0].next
        curr[1] = curr[1].next
    return curr[0]



r1 = None
for i in range(16):
    r1 = insert(r1, i)

r2 = None
for i in range(10,20):
    r2 = insert(r2, i)

r3 = None
for i in range(20,30):
    r3 = insert(r3, i)

tail(r1).next = r3
tail(r2).next = r3

r1.print()
r2.print()

intersection(r1,r2).print()

