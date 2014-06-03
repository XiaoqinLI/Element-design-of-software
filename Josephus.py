## File: Josephus.py
## Description: To make a circular linked list you need to
##              make the next field in the last link of the linked list point back to the first link
##              instead of being null. From any point in a circular list it is possible to reach any
##              other point in the list. Thus any link can be the first or last link. One useful convention
##              is to let the external pointer to the circular list point to the last link and to allow the
##              following link be the first link. We also have the convention that a null pointer represents an empty circular list. 
##              Total time consumed: 2.5 hours.

## Date Created: 03/27/2014
## Date Last Modified:03/27/2014


class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
        
class CircularList(object):
    # Constructor
    def __init__ ( self ):
      self.first = None
      
    # Add data at the beginning of the list #
    def addFirst (self, item): 
        newLink = Link(item)        # Create a new node
        self.first = newLink         # head points to the new node
        self.first.next = self.first
            
    # Add data at the end of a list #
    def addLast (self, item): 
        newLink = Link(item)
        current = self.first       
        while ( current.next != self.first):
            current = current.next 
        current.next = newLink  # Link the new with the last node      
        current = current.next      
        current.next = self.first
              
    # Insert an element in the list
    # alway add it to the last
    def insert ( self, item ):
        if self.first == None:
            self.addFirst(item)
            return
        else:
            self.addLast(item)
            return

    # Find and return the link with the given key
    # key here is a data value, return None if could not find it
    def find ( self, key ):
        current = self.first
        if current == None:
            return None
        else:
            if current.next == self.first and current.data == key:
                return current
            while ( current.next != self.first):
                if current.data == key:
                    return current
                else:
                    current = current.next
            if current.data == key:
                return current
            else:
                return None
        
    # Delete a link with a given key from circular linkedlist
    def delete ( self, key ):
        current = self.first
        previous = self.first      
        while previous.next != self.first:
            previous = previous.next
        if current == None:
            return None
        if current.next == self.first and current.data == key:
            self.first = None
            return current     
        while (current.data != key):
            if current.next == self.first:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        previous.next = current.next
        return current
            
    # Delete the nth link starting from the Link start utill the circular list is
    # emply, print all killed each line and the last one should be Josephus  
    def deleteAll ( self, start, n ):      
        starting_pos = self.first        
        while start != 1:        # head moving to start point
            starting_pos = starting_pos.next
            start -= 1
            
        current_starting = starting_pos      
        while starting_pos.next != starting_pos:
            m = n
            while m != 1:        # locate the one to be deleted
                starting_pos = starting_pos.next
                m -= 1             
            value = starting_pos.data
            deleted_link = self.delete(value)      
            print(deleted_link.data)    # print out last deleted one
            starting_pos = starting_pos.next
        print(starting_pos.data)       # print out Josephus
         
    # Return a string representation of a Circular List
    def __str__ ( self ):
        current = self.first
        if current == None:
            return "The linkedlist is empty"
        temp_result = str(current.data)
        temp_result += " "  # seperated by whitespace
        while (current.next != self.first):
            temp_result += str(current.next.data)
            current = current.next
            temp_result += " "
        result = temp_result[0:-1] 
        return result
    
def main():
    infile = open("josephus.txt")
    num_soldier = int(infile.readline())
    counting_start = int(infile.readline())
    num_elimi = int(infile.readline())
    Circularlist1 = CircularList()
    for i in range(1,num_soldier+1):
        Circularlist1.insert(i)
    if Circularlist1.first != None:
        Circularlist1.deleteAll(counting_start,num_elimi)
    else:
        print(Circularlist1)
    
main()



        

    

