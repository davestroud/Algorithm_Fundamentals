class Node:
    def __init__(self, data): # Instance attributes
        self.data = data # attribute called data
        self.next = None 
    
    # Instance method ~ dunder method
    def __repr__(self):
        return self.data
        
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None 
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                
    # Instance method ~ dunder method    
    def __repr__(self): 
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

        

        