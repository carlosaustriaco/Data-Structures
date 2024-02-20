from InsertNode import insertNode
from PrintList import printList
from RemoveNode import removeNode

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, node):
        if (self.head == None):
            self.head = node
        else:
            h = self.head

            while (h.next != None):
                h = h.next

            h.next = node

    def removeNode(self, node):
        if(self.head != None):
            prev = None
            curr = self.head

            while (curr != None):
                if (curr.data == node.data):
                    if (prev != None):
                        prev.next = curr.next
                    else:
                        self.head = curr.next    
                    
                    break

                prev = curr
                curr = curr.next

    def printList(self):
        if (self.head != None):
            h = self.head

            while(h != None):
                print(h.data)
                h = h.next

    def reverse(self):
        if (self.head == None):
            return None
        else:
            r = LinkedList()

            if (self.head.next == None):
                r.insertNode(self.head)
            else:
                prev = None
                curr = self.head
                forw = self.head.next

                while (forw != None):
                    curr.next = prev
                    prev = curr
                    curr = forw
                    forw = forw.next

                curr.next = prev

                r.insertNode(curr)

                return r
                
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

    printList(head)
