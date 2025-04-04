def loop_size(node):
    n = node
    while True:
        if not node or not node.next:
            break
        n = n.next
        node = node.next.next
        if n == node:
            break
    result = 1
    node = node.next
    while True:
        if n == node:
            break
        node = node.next
        result += 1
    return result
