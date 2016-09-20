from dubLinkList import Node
from dubLinkList import DubLinkedList

def insertHeadTest():
    print ' '
    print 'Initializing linkList1'
    linkList1 = DubLinkedList()
    print 'Inserting "Begin" at head'
    linkList1.insertHead("Begin")
    print 'Size of linkList1:'
    print linkList1.size()
    print 'Inserting "at" at head'
    linkList1.insertHead("at")
    print 'Size of linkList1:'
    print linkList1.size()
    print 'Print linkList1'
    linkList1.printList()

def insertTailTest():
    print ' '
    print 'Initializing linkList2'
    linkList2 = DubLinkedList()
    print 'Inserting "End" at tail'
    linkList2.insertTail("End")
    print 'Size of linkList2:'
    print linkList2.size()
    print 'Inserting "after" at tail'
    linkList2.insertTail("after")
    print 'Size of linkList2:'
    print linkList2.size()
    print 'Print linkList2'
    linkList2.printList()
    
def insertHeadTailTest():
    print ' '
    print 'Initializing linkList3'
    linkList3 = DubLinkedList()
    print 'Inserting "Begin" at head'
    linkList3.insertHead("Begin")
    print 'Inserting "End" at tail'
    linkList3.insertTail("End")
    print 'Print linkList3'
    linkList3.printList()
    print 'Inserting "First" at head'
    linkList3.insertHead("First")
    print 'Inserting "Second" at tail'
    linkList3.insertTail("Second")
    print 'Print linkList3'
    linkList3.printList()
 
def searchTest(): 
    print ' '
    print 'Testing search() and delete()'
    print 'Initializing linkList4'
    linkList4 = DubLinkedList()
    print 'Inserting "Begin" at head'
    linkList4.insertHead("Begin")
    print 'Inserting "End" at tail'
    linkList4.insertTail("End")
    print 'Print linkList4'
    linkList4.printList()
    print 'Inserting "First" at head'
    linkList4.insertHead("First")
    print 'Inserting "Second" at tail'
    linkList4.insertTail("Second")
    print 'Print linkList4'
    linkList4.printList()
    print 'Search for "First"'
    try:
        linkList4.search("First")
        print 'Data in list'
    except:
        print 'Data not in list'
        
    print 'Search for "Last"'
    try:
        linkList4.search("Last")
        print 'Data in list'
    except:
        print 'Data not in list'
    print 'Delete "Begin"'
    try:
        linkList4.delete("Begin")
        print 'Data in list deleted'
    except:
        print 'Data to delete not in list'
    print 'Print linkList4'
    linkList4.printList()
    print 'Delete "Start"'
    try:
        linkList4.delete("Start")
        print 'Data in list deleted'
    except:
        print 'Data to delete not in list'
    print 'Print linkList4'
    linkList4.printList()

def insertAtIndexTest():
    print ' '
    print 'Testing insertAtIndex()'
    print 'Initializing linkList5'
    linkList5 = DubLinkedList()
    print 'Inserting "first" and "second" at head'
    linkList5.insertHead("first")
    linkList5.insertHead("second")
    print 'Inserting "third" and "fourth" at tail'
    linkList5.insertTail("third")
    linkList5.insertTail("fourth")
    print 'Print linkList5'
    linkList5.printList()
    print 'Inserting "new first" at index 0'
    try:
        linkList5.insertAtIndex(0, "new first")
        print 'Print linkList5'
        linkList5.printList()
    except:
        print 'List does not contain index'
    print 'Inserting "new last" at index 4'
    try:
        linkList5.insertAtIndex(5, "new last")
        print 'Print linkList5'
        linkList5.printList()
    except:
        print 'List does not contain index'
    print 'Inserting "final" at index 7'
    try:
        linkList5.insertAtIndex(7, "final")
        print 'Print linkList5'
        linkList5.printList()
    except:
        print 'List does not contain index'
 
def insertAtValueTest():
    print ' '
    print 'Testing insertAtValue()'
    print 'Initializing linkList6'
    linkList6 = DubLinkedList()
    print 'Inserting "first" and "second" at head'
    linkList6.insertHead("first")
    linkList6.insertHead("second")
    print 'Inserting "third" and "fourth" at tail'
    linkList6.insertTail("third")
    linkList6.insertTail("fourth")
    print 'Print linkList6'
    linkList6.printList()
    print 'Inserting "new first" after second'
    try:
        linkList6.insertAtValue("second", "new first")
        print 'Print linkList6'
        linkList6.printList()
    except:
        print 'List does not contain value'
    print 'Inserting "new last" after "fourth"'
    try:
        linkList6.insertAtValue("fourth", "new last")
        print 'Print linkList6'
        linkList6.printList()
    except:
        print 'List does not contain value'
    print 'Inserting "final" after "fifth"'
    try:
        linkList6.insertAtValue("fifth", "final")
        print 'Print linkList6'
        linkList6.printList()
    except:
        print 'List does not contain value' 

insertHeadTest()
insertTailTest()
insertHeadTailTest()
searchTest()
insertAtIndexTest()
insertAtValueTest()
 