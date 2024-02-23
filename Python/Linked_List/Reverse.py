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
    