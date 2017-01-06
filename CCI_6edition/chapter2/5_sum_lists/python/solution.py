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



def sum_lists(r1,r2):
    if r1 is None:
        return r1
    if r2 is None:
        return r2

    if r1.count() < r2.count():
        s = r1
        l = r2
    else:
        s = r2
        l = r1

    root, carry = None, 0
    while s is not None:
        x = s.data + l.data + carry
        carry = int(x / 10)
        root = insert(root, x % 10)
        s, l = s.next, l.next
    while l is not None:
        x = l.data + carry
        carry = int(x / 10)
        root = insert(root, x % 10)
        l = l.next
    if 0 < carry:
        root = insert(root, carry)
    return root

def sum_lists_reversed(r1,r2):
    def sum(r1,r2):
        a = r1.next is None
        b = r2.next is None
        if a and b:
            x = [None,0]
        elif a:
            x = sum(r1,r2.next)
        elif b:
            x = sum(r1.next,r2)
        else:
            x = sum(r1.next,r2.next)

        s = r1.data + r2.data + x[1]
        a = Node(s % 10)
        if x[0] is not None:
            a.next = x[0]
        return [a, int(s/10)]
    return sum(r1,r2)[0]

r1 = None
for i in list([1,2,3,4]):
    r1 = insert(r1, i)

r2 = None
for i in list([8,9]):
    r2 = insert(r2, i)

r1.print()
r2.print()

sum_lists_reversed(r1,r2).print()

