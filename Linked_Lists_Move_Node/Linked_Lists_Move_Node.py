class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if not source:
        raise Exception
    n = Node(source.data)
    n.next = dest
    dest = n
    source = source.next
    return Context(source, dest)
