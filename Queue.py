from dubLinkList import *

class Queue(object):
    
    def __init__(self):
        self.queue = DubLinkedList()
        
    def add(self, data):
        self.queue.insertHead(data)
    
    def remove(self):
        self.queue.delete_tail()
    
    def peek(self):
        return self.queue.tail.get_data()
    
    def printList(self):
        self.queue.printList()
    
    def is_empty(self):
        if self.queue.size == 0:
            return True
        else: 
            return False

q = Queue()
print "remove" 
q.remove()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.printList()
print "peek", q.peek()
print "isEmpty", q.is_empty()
print "remove"
q.remove()
print "isEmpty", q.is_empty()
q.printList()
print "peek", q.peek()
print "remove"
q.remove()
q.printList()
print "peek", q.peek()