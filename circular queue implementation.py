#circular queue implementation
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class  CircularLinkedList:
    def __init__(self):
        self.head = None
        self.front = -1
        self.rear = -1

    def enqueue(self,data):
        ptr = Node(data)

        self.rear = ptr

        if self.head is None:
            self.head = ptr
            ptr.next = ptr
            self.front = ptr

        itr = self.head
        ptr.next = itr
        while itr.next !=self.head:
            itr = itr.next
        itr.next = ptr

    def dequeue(self):
        if self.front == -1:
            raise Exception("Queue is empty")
        itr = self.head
        if self.head.next == self.head:
            self.front =-1
            self.head = None
            return

        while itr.next!=self.head:
            itr = itr.next
        itr.next = self.head.next
        self.head = self.head.next
        self.front = self.head.data



        
    

        
    def printLinkedList(self):
        if not self.head:
            print("empty list")
            return
        itr = self.head
        while  True:
            print(str(itr.data) + " --> ",end="")
            itr = itr.next
            if itr == self.head:
                print()
                break

    def get_length(self):
        if not self.head :
            return 0
        itr = self.head
        count = 1
        while itr.next!=self.head:
            count+=1
            itr = itr.next
        return count

    
#__main__

cll = CircularLinkedList()
cll.enqueue(45)
cll.enqueue(56)
cll.enqueue(234)

cll.dequeue()
cll.dequeue()

cll.printLinkedList()
print(cll.front)
