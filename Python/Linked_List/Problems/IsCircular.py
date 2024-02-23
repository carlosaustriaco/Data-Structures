'''
The main goal is to check if the list is circular
An empty list is circular
'''

def is_circular(head):
    if (not head) or (not head.next):
        return True

    h = head
    head = head.next

    while head and (head != h):
        head = head.next

    return head == h