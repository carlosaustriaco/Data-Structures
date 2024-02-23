'''
The main goal is to count how many nodes are there in a circular linked list
'''

def circular_list_count(head):
    if not head:
        return 0

    h = head
    head = head.next
    i = 1

    while(head != h):
        i += 1
        head = head.next

    return i