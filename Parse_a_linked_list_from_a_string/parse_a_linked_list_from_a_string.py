def linked_list_from_string(s):
    lst = s.split()
    ls = [f for f in lst if f != '->']
    result = Node(int(ls[0]))
    prev = result
    for i in range(1, len(ls) - 1):
        node = Node(int(ls[i]))
        prev.next = node
        prev = node
    return result