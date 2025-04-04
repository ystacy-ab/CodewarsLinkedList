from preloaded import Node

def swap_pairs(head):
    n = Node()
    n.next = head
    prev = n
    while True:
        if not head or not head.next:
            break
        f, s = head, head.next
        prev.next = s
        f.next = s.next
        s.next = f
        prev = f
        head = f.next
    return n.next
