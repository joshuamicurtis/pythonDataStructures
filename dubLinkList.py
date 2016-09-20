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
        
    def set_prev(self, new_prev):
        self.prev_node = new_prev
        
class DubLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        
    #O(1) efficient!
    def insertHead(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)      
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        
        #O(1) efficient!
    def insertTail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node) 
            new_node.set_prev(self.tail)
        self.tail = new_node
        
    #O(n)
    def insertAtIndex(self, idx, dataInsert):
        if idx == 0:
            self.insertHead(dataInsert)
            return None
        current = self.head
        count = 0
        found = False
        while current and found is False:
            if((count+1) == idx):
                found = True
                new_node = Node(dataInsert)
                new_node.set_next(current.next_node)
                current.set_next(new_node)
            else:
                count += 1
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return None 
        
    #O(n) 
    def insertAtValue(self, dataSearch, dataInsert):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == dataSearch:
                found = True
                new_node = Node(dataInsert)
                new_node.set_next(current.next_node)
                current.set_next(new_node)
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return None
            
        #O(n)
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
     
    #O(n)
    def printList(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
        return None
        
    #O(n)
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
        
    #O(n)
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())