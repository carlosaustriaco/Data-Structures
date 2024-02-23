from InsertNode import insertNode
from PrintList import printList
from RemoveNode import removeNode
from Reverse import reverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
                
if __name__ == '__main__':
    head = None
    
    n1 = Node(1)
    n2 = Node(10)
    n3 = Node(100)
    n4 = Node(50)
    n5 = Node(12345)

    head = insertNode(head, n1)
    head = insertNode(head, n2)
    head = insertNode(head, n3)
    head = removeNode(head, n2)
    head = insertNode(head, n4)
    head = insertNode(head, n5)

    head2 = reverse(head)

    printList(head2)
