## File: TestLinkedList.py
## Description: TestLinkedList.The purpose of this work is to
##              write helper methods for the data structure LinkedList class that
##              we developed and test them.  For the time being assume that the data
##              that we are handling are integers.Later on when we use objects of 
##              other classes we will write compare functions for those classes.
##              All corner test have been passed.
## Author: Xiaoqin LI
## Date Created: 03/22/2014
## Date Last Modified:03/25/2014

import random

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
        
class LinkedList (object):
    def __init__ (self):
        self.first = None
        
    # get number of links #
    def getNumLinks (self):
        size = 0
        current = self.first
        while (current != None):
            size += 1
            current = current.next
        return size
  
    # Add data at the beginning of the list #
    def addFirst (self, data): 
        newLink = Link (data)        # Create a new node
        newLink.next = self.first    # link the new node with the head
        self.first = newLink         # head points to the new node
            
    # Add data at the end of a list #
    def addLast (self, data): 
        newLink = Link (data)
        current = self.first   
        if current == None:
            self.first = newLink      # the new node is the only node in list
            return       
        while ( current.next != None):
            current = current.next 
        current.next = newLink  # Link the new with the last node
        
    # Add data in an ordered list in ascending order 
    def addInOrder (self, data):
        if self.first == None:
            self.addFirst(data)
            return
        if data < self.first.data:
            self.addFirst(data)
            return
        else:
            newLink = Link(data)
            current = self.first
            previous = self.first
            while (data > current.data):
                if current.next == None:
                    self.addLast(data)
                    return
                else:
                    previous = current
                    current = current.next
            previous.next = newLink
            newLink.next = current
                
    # Search in an unordered list, return None if not found #
    def findUnordered (self, data):   # searches through the entire list.
        current = self.first
        if current == None:
            return None
        else:
            while (current.data != data):
                if current.next == None:
                    return None
                else:
                    current = current.next
            return current

    # Search in an ordered list, return None if not found #
    def findOrdered (self, data):                                     
        current = self.first
        if current == None:
            return None
        else:
            while (current.data != data):
                if current.next == None:
                    return None
                else:
                    if current.next.data > data: # stops its search when it finds a link with
                        return None              # bigger value than the data 
                    else:
                        current = current.next
            return current

    # Delete and return Link from an unordered list or None if not found #
    def delete (self, data):
        current = self.first
        previous = self.first
        if current == None:
            return None
        
        while (current.data != data):
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:   # to delete current link, just link previous one to next one
            self.first = self.first.next
        else:
            previous.next = current.next
        return current

    # String representation of data 10 items to a line, 2 spaces between data #
    def __str__ (self):
        current = self.first
        if current == None:
            return "The linkedlist is empty"
        count = 0
        result = ""
        while current!= None:
            result += str(current.data)
            current = current.next
            count +=1
            if count % 10 != 0:   # 10 elements each line, seperated by whitespace
                result += "  "
            else:
                result += '\n'
        if  result[-1]  == '\n':
            return result[0:-1]   # do not print this extra new line
        else:
            return result         

    # Copy the contents of a list and return new list #
    def copyList (self):
        copy_LinkedList = LinkedList()
        current = self.first
        while (current != None):
            copy_LinkedList.addLast(current.data)
            current = current.next
        return copy_LinkedList

    # Reverse the contents of a list and return new list #
    def reverseList (self):
        reverse_LinkedList = LinkedList()
        current = self.first
        while (current != None):       
            reverse_LinkedList.addFirst(current.data)
            current = current.next
        return reverse_LinkedList

    # Sort the contents of a list in ascending order and return new list #
    def sortList (self):
        sortedList = LinkedList()     
        if self.getNumLinks() == 0:
            return sortedList           # return this empty list, no need to be sorted
        current = self.first
        sortedList.addFirst(current.data)
        current = current.next
        while (current != None):            
            current_sorted = sortedList.first
            previous_sorted = sortedList.first
            if current.data <= current_sorted.data: # insert at head if it is lower than current sorted head
                sortedList.addFirst(current.data)
            else:
                while(current.data > current_sorted.data):
                    if current_sorted.next == None:
                        sortedList.addLast(current.data)
                        break
                    else:                    
                        previous_sorted = current_sorted
                        current_sorted = current_sorted.next
                        if current.data <= current_sorted.data:  # link it up at right place
                            newLink = Link(current.data)
                            previous_sorted.next = newLink
                            newLink.next = current_sorted            
            current = current.next
        return sortedList
        
    # Return True if a list is sorted in ascending order or False otherwise #
    def isSorted (self):
        if self.getNumLinks() < 2:
            return True
        current = self.first
        previous = self.first
        while current.next != None:
            previous = current
            current = current.next
            if previous.data > current.data:
                return False
        return True
            
    # Return True if a list is empty or False otherwise #
    def isEmpty (self):
        return (self.getNumLinks() == 0)

    # Merge two sorted lists and return new list in ascending order #
    def mergeList (self, b):
        merged_List = LinkedList()
        current_self = self.first
        current_b = b.first
        while (current_self != None and current_b != None):
            if current_self.data < current_b.data:
                merged_List.addLast(current_self.data)
                current_self = current_self.next
            else:
                merged_List.addLast(current_b.data)
                current_b = current_b.next
        while (current_self != None):
            merged_List.addLast(current_self.data)
            current_self = current_self.next
        while (current_b != None):
            merged_List.addLast(current_b.data)
            current_b = current_b.next
        return merged_List
                
    # Test if two lists are equal, item by item and return True #
    def isEqual (self, b):
        if self.getNumLinks() == 0 and b.getNumLinks() == 0:
            return True
        if self.getNumLinks() != b.getNumLinks():
            return False
        else:
            current_s = self.first
            current_b = b.first
            while current_s != None:
                if current_s.data != current_b.data:
                    return False
                current_s = current_s.next
                current_b = current_b.next          
            return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.#
    def removeDuplicates (self):
        data_list = []
        Unique_List = LinkedList()
        current = self.first
        while (current != None):
            if current.data not in data_list:
                Unique_List.addLast(current.data)
                data_list.append(current.data)        
            current = current.next
        return Unique_List
        
def main():
    # Test methods addFirst() and __str__() by adding more than
    # 10 items to a list and printing it.
    print("Test methods addFirst() and __str__()")
    print("add 25 items randomly picked up between 1-100 to Linkedlist1")
    print("The Linkedlist1 is: ")
    Linkedlist1 = LinkedList()

    for i in range(25):
        Linkedlist1.addFirst(random.randint(1,100))
    print(Linkedlist1)
    print()
    
    # Test method addLast()
    print("Test method addLast() by adding 1000 at the end of Linkedlist1")
    Linkedlist1.addLast(1000)
    print(Linkedlist1)
    print()
    
    # Test method getNumLinks()
    print("Test method getNumLinks()")
    print("the number of links in Linkedlist1 is:", Linkedlist1.getNumLinks())
    print()
    
    # Test method findUnordered() 
    # Consider two cases - item is there, item is not there
    print("Test method findUnordered()")
    print("Finding 1000 from LinkedList1: ")
    print(Linkedlist1.findUnordered(1000))
    print("Finding 2000 from LinkedList1: ")
    print(Linkedlist1.findUnordered(2000))
    print()

    # Test method findOrdered() 
    # Consider two cases - item is there, item is not there
    print("Test method findordered()")
    print("Finding 1000 from LinkedList1: ")
    print(Linkedlist1.findOrdered(1000))
    print("Finding 2000 from LinkedList1: ")
    print(Linkedlist1.findOrdered(2000))
    print()
    
    # Test method delete()
    # Consider two cases - item is there, item is not there
    print("Test method delete()")
    print("Deleting 1000 from LinkedList1: ")
    print( Linkedlist1.delete(1000))
    print("Deleting 2000 from LinkedList1: ")
    print( Linkedlist1.delete(2000))
    print()
      
    # Test method getNumLinks()
    print("Test method getNumLinks()")
    print("the number of links in Linkedlist1 is:", Linkedlist1.getNumLinks())
    print()

    # Test method copyList()
    print("Test method copyList(), Linkedlist2 copies from Linkedlist1.")
    print("Linkedlist2 is: ")
    Linkedlist2 = Linkedlist1.copyList()
    print(Linkedlist2)
    print()
    
    # Test method reverseList()
    print("Test method reverseList(), Linkedlist3 is a reversed Linkedlist1.")
    print("Linkedlist3 is: ")
    Linkedlist3 = Linkedlist1.reverseList()
    print(Linkedlist3)
    print()
    
    # Test method sortList()
    print("Test method sortList(), Linkedlist4 is a sorted Linkedlist1.")
    print("Linkedlist4 is: ")
    Linkedlist4 = Linkedlist1.sortList()
    print(Linkedlist4)
    print()

    # Test method addInOrder()
    print("Test method addInOrder(), Linkedlist4 is sorted")
    Linkedlist4.addInOrder(50)
    print("After adding a new link(50) in order, now Linkedlist4 is: ")
    print(Linkedlist4)
    print()
    
    # Test method isSorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Test method isSorted()")
    print("Is Linkedlist1 is sorted: ")
    print((Linkedlist1.isSorted()))
    print("Is Linkedlist4 is sorted: ")
    print((Linkedlist4.isSorted()))
    print()

    # Test method isEmpty()
    # Return True if a list is empty or False otherwise
    print("Test method isSorted()")
    print("Is Linkedlist1 is empty: ")
    print((Linkedlist1.isEmpty()))
    print("Is Linkedlist4 is empty: ")
    print((Linkedlist4.isEmpty()))
    print()
    
    # Test method isEqual()
    # Consider two cases - lists are equal, lists are not equal
    print("Test method isEqual()")
    print("Is Linkedlist1 equal to Linkedlist2: ")
    print((Linkedlist1.isEqual(Linkedlist2)))
    print("Is Linkedlist1 equal to Linkedlist4: ")
    print((Linkedlist1.isEqual(Linkedlist4)))
    print()
    
    # Test method mergeList()
    print("Test method mergeList()")
    print("Linkedlist1 merging Linkedlist4: ")
    print(Linkedlist1.mergeList(Linkedlist4))
    print()
    
    # Test removeDuplicates()
    print("Test method removeDuplicates()")
    print("Linkedlist1(Before): ")
    print(Linkedlist1)
    print("Linkedlist1(After)")
    print(Linkedlist1.removeDuplicates())
    
main()
    

