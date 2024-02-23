def printList(head):
    while(head != None):
        print(head.data)
        head = head.next

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

def reverse(head):
    if (head == None):
        return None
    
    if (head.next == None):
        return head
    
    prev = None
    curr = head
    forw = head.next

    while (forw != None):
        curr.next = prev
        prev = curr
        curr = forw
        forw = forw.next

    curr.next = prev

    return curr
    
def search(head, data):
    if not head:
        return False

    h = head

    while head:
        if head.data == data:
            return True

        head = head.next

    return False

def count(head):
    i = 0

    while(head):
        i += 1
        head = head.next

    return i