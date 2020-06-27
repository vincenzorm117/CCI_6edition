
class LRUCacheNode:
    def __init__(self, key, data):
        self.prev = None
        self.next = None
        self.key = key
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


class LRUCache:

    def __init__(self, size):
        if type(size) != int or size <= 0:
            raise Exception('Argument must be a positive int.')
        self.size = size
        self.map = {}
        self.head = None
        self.tail = None

    def moveToTop(self, node):
        if node == None:
            return
        if node == self.head:
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.head.prev = None


    def updateUsed(self, node):
        self.swapNodes(node, self.head)

    def swapNodes(self, nodeA, nodeB):
        if nodeA == None or nodeB == None:
            raise Exception('Require two LRUCacheNode nodes as arguments.')
        tmpData = nodeA.data
        tmpKey = nodeA.key
        nodeA.data = nodeB.data
        nodeA.key = nodeB.key
        nodeB.data = tmpData
        nodeB.key = tmpKey
        self.map[nodeA.key] = nodeA
        self.map[nodeB.key] = nodeB


    def get(self, key):
        if key in self.map:
            node = self.map[key]
            data = node.data
            self.moveToTop(node)
            return data
        else:
            return None


    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.data = value
            self.moveToTop(node)
        else:
            if len(self.map) < self.size:
                node = LRUCacheNode(key, value)
                if self.head == None:
                    self.head = node
                    self.tail = self.head
                    self.map[key] = self.head
                else:
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                    self.map[key] = self.head
            else:
                self.remove(self.tail.key)
                self.set(key, value)

        return self

    def remove(self, key):
        node = self.map[key]
        if node != None:
            del self.map[key]
            # Case: only one node
            if node.prev == None and node.next == None:
                del node
                self.head = None
                self.tail = None
            # Case: node is head, but not tail
            elif node.prev == None and node.next != None:
                self.head = node.next
                self.head.prev = None
                del node
            # Case: node is tail
            elif node.prev != None and node.next == None:
                self.tail = node.prev
                self.tail.next = None
                del node
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                del node

        return self




    def print(self):
        print('Map: %s' % (self.map))
        print('LinkedList: ', end=' ')
        node = self.head
        if node != None:
            print(node.data, end='')
            node = node.next
            while node != None:
                print(', ', end='')
                print(node.data, end='')
                node = node.next
            print()
        else:
            print('Empty')



testcases = [
    (10, list(range(20))),
    (10, [0,1,2,3,4,5,6,7,5,5,2,8,8,8,8,8,10,12,13])
]

for size, array in testcases:
    print('=' * 100)
    print('Testcase: ', end='')
    print(size, array)
    cache = LRUCache(size)
    for i in array:
        print(i)
        cache.set(i, i)
        cache.print()
        print()
