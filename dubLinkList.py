class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
    def get_prev(self):
        return self.prev_node
        
class DubLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def 