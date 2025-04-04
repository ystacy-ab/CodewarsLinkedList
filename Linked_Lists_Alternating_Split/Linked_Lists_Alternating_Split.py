class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise Exception
    first = f = Node()
    second = s = Node()
    check = True
    while True:
        if not head:
            break
        if check:
            f.next = head
            f = f.next
        else:
            s.next = head
            s = s.next
        head = head.next
        check = not check
    f.next = None
    s.next = None
    return Context(first.next, second.next)
