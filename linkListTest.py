from linkList import Node
from linkList import LinkedList

print 'Testing linkList.py'

print 'Initializing linkList1'
linkList1 = LinkedList()

print 'Inserting "Hello" at head'
linkList1.insertHead("Hello")

print 'Size of linkList1:'
print linkList1.size()

print 'Inserting "world!" at head'
linkList1.insertHead("world")

print 'Size of linkList1:'
print linkList1.size()

print 'Search for "Hello"'
try:
    linkList1.search("Hello")
    print 'Data in list'
except:
    print 'Data not in list'
    
print 'Search for "hello"'
try:
    linkList1.search("hello")
    print 'Data in list'
except:
    print 'Data not in list'

print 'Inserting "DOG" at head'
linkList1.insertHead("DOG")

print 'Size of linkList1:'
print linkList1.size()   

print 'Delete "Hello"'
try:
    linkList1.delete("Hello")
    print 'Data in list'
except:
    print 'Data not in list'

print 'Size of linkList1:'
print linkList1.size()

print 'Delete "CAT"'
try:
    linkList1.delete("CAT")
    print 'Data in list'
except:
    print 'Data not in list'
    
print 'Size of linkList1:'
print linkList1.size()

print 'Print list'
linkList1.printList()

print 'Insert "Bone" after "DOG"'
try: 
    linkList1.insertAtValue("DOG", "Bone")
    print "New list is:"
    linkList1.printList()
except:
    print 'Insert at data not in list'
    
print 'Insert "food" after "dog"'
try: 
    linkList1.insertAtValue("dog", "food")
    print "New list is:"
    linkList1.printList()
except:
    print 'Searched data not in list'
    
print 'Insert "peace" at index 2'
try:
    linkList1.insertAtIndex(2, "peace")
    print "New list is:"
    linkList1.printList()
except:
    print 'List does not contain index'
    
print 'Insert "endEdge" at index 4'
try:
    linkList1.insertAtIndex(4, "endEdge")
    print "New list is:"
    linkList1.printList()
except:
    print 'List does not contain index'

print 'Insert "startEdge" at index 0'
try:
    linkList1.insertAtIndex(0, "startEdge")
    print "New list is:"
    linkList1.printList()
except:
    print 'List does not contain index'
    
print 'Insert "test" at tail value'
linkList1.insertAtValue("endEdge", "test")
print "New list is:"
linkList1.printList()