'''
EASY PROBLEMS
'''

''''
Given a list, find the middle of it
https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
'''
def get_middle(head):
    s = head
    f = head

    while f and (f.next):
        s = s.next
        f = f.next.next

    return s.data

'''
The main goal is to check if the list is circular
An empty list is circular
https://www.geeksforgeeks.org/check-if-a-linked-list-is-circular-linked-list/
'''
def is_circular(head):
    if (not head) or (not head.next):
        return True

    h = head
    head = head.next

    while head and (head != h):
        head = head.next

    return head == h

'''
The main goal is to count how many nodes are there in a circular linked list
https://www.geeksforgeeks.org/count-nodes-circular-linked-list/
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

'''
The main goal is to convert a single list into a circular list
https://www.geeksforgeeks.org/convert-singly-linked-list-circular-linked-list/
'''
def convert_to_circular(head):
    if not head:
        return head
    
    h = head

    while (head.next):
        head = head.next

    head.next = h

'''
The main goal is to exchange the last element of a circular list with the first
one.
https://www.geeksforgeeks.org/exchange-first-last-node-circular-linked-list/
'''
def exchange_first_last_circular(head):
    if (not head) or (not head.next):
        return head

    h = head
    prev = head
    curr = head.next

    while curr != h:
        prev = curr
        curr = curr.next

    t = curr.data
    curr.data = prev.data
    prev.data = t

    return h

'''
Function to print a circular list
'''
def print_circular_list(head):
    if not head:
        return

    h = head
    
    print(head.data)
    head = head.next

    while(head != h):
        print(head.data)
        head = head.next

'''
The main goal is to detect if the linked list has cycles
https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/
'''
def detect_cycle(head):
    if (not head) or (not head.next):
        return False

    s = head.next
    f = head.next.next

    while f and f.next and (f != s):
        f = f.next.next
        s = s.next

    if (f and f.next):
        return True
    else:
        return False

'''
Function to get the length of a cycle
https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/
'''
def get_cycle_length(head):
    if not head:
        return 0

    if not head.next:
        return 1

    s = head.next
    f = head.next.next

    while f and f.next and f != s:
        f = f.next.next
        s = s.next

    if (not f) or (not f.next):
        return 0

    p = s
    s = s.next
    count = 1

    while s != p:
        count += 1
        s = s.next

    return count

