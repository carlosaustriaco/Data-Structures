def removeNode(head, node):
    if (head != None):            
        prev = None
        curr = head
        
        while (curr != None):
            if (curr.data == node.data):
                if (prev != None):
                    prev.next = curr.next
                else:
                    head = curr.next
                
                break
            
            prev = curr
            curr = curr.next

        return head