#!/usr/local/bin/python3

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


def has_loop(root):
    if root.next is None:
        return False
    slow = root
    fast = root

    while True:
        if fast.next is None or fast.next.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True



def loop_detection(root):
    if root.next is None:
        return None
    n1 = root #slow node
    n2 = root #fast node (2x speed of n1)

    while True:
        if n2.next is None or n2.next.next is None:
            return False
        n1 = n1.next
        n2 = n2.next.next
        if n1 == n2:
            break
    n2 = root
    while n2 != n1:
        n2 = n2.next
        n1 = n1.next
    return n1


root = None
data = list(range(11))

for i in data:
    root = insert(root,i)
root.print()

t = tail(root)
some = find(root,3)
t.next = some

print(loop_detection(root).data)
