class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        
    #O(1) efficient!
    def insertHead(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)      
        if self.head is None:
            print "first head is first tail"
            self.tail = new_node
        self.head = new_node
        
    #O(1) efficient!
    def insertTail(self, data):
        new_node = Node(data)
        if self.tail is None:
            print "first tail is first head"
            self.head = new_node
        else:
            self.tail.set_next(new_node) 
        self.tail = new_node
            