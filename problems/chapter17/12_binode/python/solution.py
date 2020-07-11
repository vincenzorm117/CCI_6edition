###################################
# Helpers

class BinTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root == None:
            self.root = BiNode(data)
            return

        currNode = self.root
        while True:
            if data < currNode.data:
                if currNode.node1 == None:
                    currNode.node1 = BiNode(data)
                    return
                else:
                    currNode = currNode.node1
            else:
                if currNode.node2 == None:
                    currNode.node2 = BiNode(data)
                    return
                else:
                    currNode = currNode.node2


class BiNode:
    node1 = None
    node2 = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

###################################
# Solutions

def solution_recursive(binode):
    last = None
    def recurse(binode):
        nonlocal last
        if binode == None:
            return
        recurse(binode.node1)
        binode.node1 = last
        last = binode
        recurse(binode.node2)
    recurse(binode)

    tail = last
    head = last
    head.node2 = None
    currNode = head.node1
    while currNode != None:
        currNode.node2 = head
        head = currNode
        currNode = currNode.node1

    return (head, tail)


def solution_iterative(binode):
    if binode == None:
        return

    last = None
    stack = [(binode, False)]
    while len(stack) > 0:
        currBinode, shouldProcess = stack.pop()
        if shouldProcess:
            currBinode.node1 = last
            last = currBinode
        else:
            if currBinode.node2 != None:
                stack.append((currBinode.node2, False))
            stack.append((currBinode, True))
            if currBinode.node1 != None:
                stack.append((currBinode.node1, False))

    tail = last
    head = last
    head.node2 = None
    currNode = head.node1
    while currNode != None:
        currNode.node2 = head
        head = currNode
        currNode = currNode.node1

    return (head, tail)



###################################
# Testing

def checkSolution(head, tail):
    print('============================')
    currNode = head
    while currNode != None:
        print(currNode.data, end=' ')
        if currNode.node2 != None:
            if currNode.data > currNode.node2.data:
                return False
        currNode = currNode.node2
    print()

    currNode = tail
    while currNode != None:
        print(currNode.data, end=' ')
        if currNode.node1 != None:
            if currNode.data < currNode.node1.data:
                return False
        currNode = currNode.node1
    print()
    return True

testcases = [
    [4],
    [4,2],
    [4,6],
    [4,2,6],
    [4,2,1],
    [4,2,3],
    [4,6,5],
    [4,6,7],
    [4,2,1,3],
    [4,6,5,7],
    [4,2,6,1],
    [4,2,6,3],
    [4,2,6,5],
    [4,2,6,7],
    [4,2,6,1,3],
    [4,2,6,5,7],
    [4,2,6,1,5],
    [4,2,6,1,7],
    [4,2,6,3,5],
    [4,2,6,3,7],
    [4,2,6,1,5,7],
    [4,2,6,3,5,7],
    [4,2,6,1,3,5],
    [4,2,6,1,3,7],
    [4,2,6,1,3,5,7],
    [4,2,5,1,3,6,0],
]

for testcase in testcases:
    # Setup binary search tree for testcase
    tree = BinTree()
    for item in testcase:
        tree.add(item)

    head, tail = solution_iterative(tree.root)
    assert(checkSolution(head, tail))

