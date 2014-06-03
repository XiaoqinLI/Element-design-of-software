class DoubleListNode:
    def __init__(self,data):
        self.data=data
        self.prev = None
        self.next= None

class ListIterator:
    def __init__(self):
        self._current = self.head

    def __iter__(self):
        return self

    def next(self):
        if self.size == 0 :
            raise StopIteration
        else:
            item = self._current.data
            self._current=self._current.next
            return item

class DoublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        self.size = 0
    def add(self,data):
        newnode= DoubleListNode(data)
        self.size+=1
        if self.head is None:
            self.head = newnode
            self.tail = self.head
        elif data < self.head.data: # before head
            newnode.next = self.head
            self.head.prev= newnode
            self.head= newnode
        elif data > self.tail.data: # at the end
            newnode.prev= self.tail
            self.tail.next= newnode
            self.tail=newnode
        else:
            curNode = self.head
            while curNode is not None and curNode.data < data:
                curNode=curNode.next            
            newnode.next= curNode
            newnode.prev=curNode.prev
            curNode.prev.next= newnode
            curNode.prev=newnode
    def remove(self,data):
        curNode=self.head
        while curNode is not None and curNode.data!= data:
            curNode= curNode.next
        if curNode is not None:
            self.size -= 1
            if curNode is self.head:
                self.head= curNode.next
            else:
                curNode.prev.next=curNode.next
            if curNode is self.tail:
                self.tail=curNode.prev
            else:
                curNode.next.prev=curNode.prev
        else: return None

