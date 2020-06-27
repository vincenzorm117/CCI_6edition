
#include <iostream>
#include <map>
#include <stdio.h>
#include <stack>


using namespace std;


typedef struct Node {
    Node *a;
    Node *b;
} Node;


typedef map<Node *, Node *> NodeMap;


Node *createNode() {
    Node *node = new Node;
    node->a = NULL;
    node->b = NULL;
    return node;
}


Node *_copyNode(Node *node, NodeMap &nodeMap) {
    if( node == NULL ) return NULL;

    NodeMap::iterator i = nodeMap.find(node);
    if( i != nodeMap.end() ) {
        return i->second;
    }

    Node *newNode = createNode();
    nodeMap[newNode] = node;
    newNode->a = _copyNode(node->a, nodeMap);
    newNode->b = _copyNode(node->b, nodeMap);
    return newNode;
}

Node *copyNode(Node *node) {
    if( node == NULL ) return NULL;
    NodeMap n;
    return _copyNode(node, n);
}

void printAddresses(Node *node) {
    if( node == NULL ) return;
    printf("0x%p\n", (void *)node);
    printAddresses(node->a);
    printAddresses(node->b);
}

int main() {
    Node *a = createNode();
    a->a = createNode();
    a->a->a = createNode();
    a->a->b = createNode();
    a->b = createNode();
    cout << "node: a" << endl;
    printAddresses(a);
    Node *b = copyNode(a);
    cout << "node: b" << endl;
    printAddresses(b);
}
