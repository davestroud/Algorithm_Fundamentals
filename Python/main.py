class LinkedList:
    def __init__(self):
        self.head = None
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

llist = LinkedList()
llist

first_node = Node("a")
llist.head = first_node
llist

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
llist

def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next