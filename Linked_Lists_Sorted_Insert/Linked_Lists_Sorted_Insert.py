""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    new = Node(data)
    n, n.next = Node(0), head
    prev = n
    while head and head.data < data:
        prev = head
        head = head.next
    prev.next = new
    new.next = head
    return n.next