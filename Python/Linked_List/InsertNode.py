def insertNode(head, node):
    if (head == None):
        head = node
        
        return head
    else:
        h = head

        while (head.next != None):
            head = head.next

        head.next = node
        
        return h