'''
link : https://www.geeksforgeeks.org/circular-linked-list/


question - https://www.geeksforgeeks.org/josephus-circle-using-circular-linked-list/

            circular queue implementation

'''




class  Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class circularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node_at_begining(self,data):
        ptr = Node(data)
        temp = self.head

        ptr.next = self.head

        if self.head is not None:
            while temp.next !=self.head :
                temp = temp.next 
            temp.next = ptr
        else:
             ptr.next =  ptr 
        self.head  = ptr


        
    def printLinkedList(self):
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

    def split_two_halves(self,head1,head2):
        if self.head is None:
            return
        slow = self.head
        fast = self.head

        while fast.next!=self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        head1.head = self.head
        head2.head = slow.next


        if fast.next.next == self.head:
            fast = fast.next
        # Make second half circular
        fast.next = slow.next
     
        # Make first half circular
        slow.next = self.head
            
    
    def josephus_circle(self,n,k):
        itr = self.head
        itr2 = self.head
        while self.get_length()!=1:
            for i in range(k-1):
                itr2 = itr
                itr = itr.next
            itr2.next  = itr.next
            itr = itr2.next
        return itr.data





    


#__main__
cll = circularLinkedList()    
cll.insert_node_at_begining(12)
cll.insert_node_at_begining(2)
cll.insert_node_at_begining(232)
cll.insert_node_at_begining(400)
# cll.insert_node_at_begining(300)
# cll.insert_node_at_begining(60)

# cl1 = circularLinkedList()
# cl2 = circularLinkedList()


cll.printLinkedList()
# print(cll.get_length())

# cll.split_two_halves(cl1,cl2)
# cl1.printLinkedList()
# cl2.printLinkedList() 
print(cll.josephus_circle(4,2))

