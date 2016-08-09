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
    def __init__(self, head=None):
        self.head = head
    
    #O(1) efficient!
    def insertHead(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
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
    
    
        