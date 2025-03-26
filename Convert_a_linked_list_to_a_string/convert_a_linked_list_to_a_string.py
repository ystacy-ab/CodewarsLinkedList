def stringify(node):
    s = node
    result = ''
    while s:
        result += str(s.data) + ' -> '
        s = s.next
    result += 'None'
    return result
