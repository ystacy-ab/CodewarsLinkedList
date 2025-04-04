class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head or not head.next:
        return head
    head_new = head.next
    n = reverse(head_new)
    head.next.next = head
    head.next = None
    return n