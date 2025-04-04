class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    new = head
    while True:
        if not new or not new.next:
            break
        if new.data == new.next.data:
            new.next = new.next.next
        else:
            new = new.next
    return head
