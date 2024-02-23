''''
Given a list, find the middle of it
'''

def get_middle(head):
    s = head
    f = head

    while f and (f.next):
        s = s.next
        f = f.next.next

    return s.data