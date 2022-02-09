# LinkedList Implementation with a que

'''types 
        Singular ,doubly or circular linked lists
    
    -> Advantages over arrays -  1.dynamic size 2.ease of insertion/deletion.
    -> Disavantages - 1.random access is not allowed 2. extra space for pointer required.

    -> LL representation in two part 
                -> Data
                -> pointer/reference

    -> Insertion of 3 types 
        1. Insert at begining 
                def insert_at_beging(node):
                    node = Node(data,Linkedlist().head)
                    LinkedList().head = node
        2. Insert at ending 
            if self.head = None:
                self.head = Node(data,None)
            else : 
                itr = self.head
                while itr :
                    itr = itr.next
                itr.next = Node(data,None)


        3. Insert after a given node
                itr = self.head
                while itr.data != data:
                    itr = itr.next
                itr.next = Node(data,itr.next)


    -> Deletion of a node
            Find the previous node of node to be deleted
            update the next value of that node to prev.next.next.

    ->Deleting node at a given position 
            well iterate till the given position-1
            now set itr.next = itr.next.next

    ->  Deleting complete LinkedList
            call delete node function until self.head == None

    -> Find Length of a linked List
            itr = self.head
            take count = 0 do count +=1 and itr =  itr.next while itr !=None

    -> Searching a node by value
            while itr and itr.data!=value:
                itr = itr.next
            if itr return true else False
    
    -> Get Nth node from a Linked_List
            count = 0
            while itr
                if count == index then return itr node;
                else: count+=1 and itr = itr.next;


    -> to detect if there's a loop in a given linked list or not, this will be true if we found any node twice while iterating through it'
            unique = set()
            while itr:
                if itr in unique: return True
                else : unique.add(itr) and itr.next 
        
    -> Detecting and removing a loop - Floyds cycle detection algorithm is used to do this task
            we will create two pointers slow and fast and slow will move with one step and fast will move with 2 steps 
            if at any time fast == slow that means there will be a loop otherwise will will reach None implying no Loop.

            Now after detecting the existing of loop we need to detect the node which causes the loop.
            we will do this putting two pointers one at head and another at point where slow and fast met, we will move both pointers one by one and the place where they meet will be the cause of loop 

    -> swaping nodes without swaping data
            function given below

    -> swaping nodes pairwise using data
            while itr and itr.next: 
                itr.data,itr.next.data = itr.next.data,itr.data
                itr = itr.next.next

    -> move last element to the front
            temp = self.head
            while itr.next:
                 second_last = itr and itr = itr.next
            second_last.next = None     #otherwise list will become circular
            itr.next = temp
            self.head = itr.next
    
    -> common of two sorted linked list i.e., common elements of two sorted LL's.
            dummy =  Node() and tail = dummy and dummy.next = None
            while l1 and l2:
                if (l1.data ==l2.data) =>{ new_LL.next = Node(l1.data,None) }
                elif(l1.data>l2.data)=>{l2 = l2.next}
                else : l1.next
            return dummy.next
    

    -> interesction point of two LL's ie. the common node between both linkedlists
            calculated the diff 'd' betwween number of nodes of two LL's
            traverse bigger list 'L1' till d and store Nodes in a set "uniq"
            for range(len(L1)):
                  traveserse both L1 and L2 if crrent_Node present in uniq then return else append every Node of both lists to uniq 

    -> reverse a linked List
        prev = None
        while itr:
            next = itr.next
            itr.next = prev
            prev = current
            itr = next
        self.head = prev
            
    '''

'''Geek for Geeks Link -  https://www.geeksforgeeks.org/data-structures/linked-list/'''



'''time complexity
    >> Traversal - O(n)
    >> Accesing element by value - O(n)

    '''
from random import random


class Node : 
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node  = Node(data,self.head)
        self.head = node

    def insert_at_ending(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        node = Node(data)
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_ending(data)
    

    def get_length(self):
        count = 0 
        itr =  self.head
        while itr:
            count+=1
            itr = itr.next
        return count


    def print(self):
        if self.head is None:
            print("List is empty")
            return

        llstr = ''
        itr = self.head
        while itr:
            llstr+= str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at(self,index,data):
        if index<0 or index > self.get_length():
            raise  Exception("Invalid Index")
        if index==0:
            self.insert_at_begining(data)
            return
        elif index==self.get_length():
            self.insert_at_ending(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1


    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0 
        itr = self.head
        while itr : 
            if count == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count+=1

    def insert_after_by_value(self,value,data):
        itr = self.head
        while itr.data and itr.data != value:
            itr = itr.next
        node = Node(data,itr.next)
        if itr.data :
            itr.next = node
        else:
            raise Exception("Value does not exist in the given Linked List")
    
    def remove_by_value(self,value):
        itr= self.head 
        if not self.head:
            raise Exception("Empty list")
        if self.head.data==value:
            self.head = self.head.next
            return
        while itr.next and itr.next.data != value:
            itr = itr.next
        if itr.next:
            itr.next = itr.next.next
        else:
            raise Exception("No such Value found")

    def delete_list(self):
        itr = self.head
        while itr :
            prev = itr.next
            self.remove_by_value(itr.data)
            itr = prev
        
    def search_node(self,data):
        itr = self.head
        index = 0
        while itr and itr.data!= data:
            index+=1
            itr = itr.next
        if itr :
            return index
        else:
            return index

    def get_nth_node(self,index):
        itr =self.head
        count = 0
        while itr:
            if count ==index:
                return itr.data
            count+=1
            itr = itr.next

    def get_nth_node_from_last(self,number):
        length = self.get_length()
        if number> length:
            raise Exception("index out of range")
            return
        return self.get_nth_node(length - number )

    def middle_element(self):
        length = self.get_length()
        if length == 0:
            print("list is empty")
            return
        if length%2 == 0:
            return (self.get_nth_node(length//2),self.get_nth_node(length//2-1))
        return self.get_nth_node(length//2)
    
    def detect_loop(self):
        itr = self.head
        unique = set()
        while itr : 
            if itr in unique:
                raise Exception(" Loop detected in your Linked List")
            unique.add(itr)
            itr = itr.next
        return False

    
    def detect_loop_floyds_algo(self):
        slow  = self.head
        fast = self.head
        flag = True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                print("Loop exists")
                return self.remove_loop(slow)
    
    def remove_loop(self,temp):
        start = temp
        k=0
        while start.next!=temp:
            start = start.next
            k+=1
        start.next = None
        return (k,start.data)
    
    def check_palindrome(self):
        stack_str = ""
        itr = self.head
        while itr:
            stack_str+=str(itr.data)
            itr = itr.next
        if stack_str[::-1] == stack_str:
            return True
        return False

    def swap_nodes(self,node1,node2):
        itr1 = self.head
        prev1 = None
        while itr1 and itr1 != node1 :
            prev1 = itr1
            itr1 = itr1.next
        
        itr2 = self.head
        prev2 = None
        while itr2 and node2!=itr2:
            prev2 = itr2
            itr2 = itr2.next
        if itr2 and itr1:
            if prev1 and prev2:
                prev1.next, prev2.next = itr2, itr1
                node1.next, node2.next = node2.next, node1.next
            elif prev2:
                prev2.next = itr1
                self.head = itr2                
                itr1.next,itr2.next = itr2.next,itr1.next

            else:
                prev1.next = itr2
                self.head = itr1
                itr1.next,itr2.next = itr2.next,itr1.next

    def intersection_sorted_LL(self,l1,l2):
        dummy = Node()
        tail = dummy
        while l1 and l2:
            if l1.data == l2.data:
                tail.next = Node(l1.data,tail.next)
                tail = tail.next
                l1 = l1.next
                l2 = l2.next
            elif l1.data>l2.data:
                l2 = l2.next
            else:
                l1 = l1.next
        return dummy.next
        
    
'''Count the number of occurances of a given element'''  #it is outside class just for fun😉 
def occur_of_int(item,ll):
    
    header = ll.head
    count = 0
    while header:
        if header.data == item:
            count+=1
        header = header.next
    return count

def printa(ll):
    while ll:
        print(ll.data)
        ll = ll.next

if __name__ == '__main__':
    ll =LinkedList()
    ll.insert_at_begining(900)
    ll.insert_at_begining(89)
    ll.insert_at_begining(34)
    ll.insert_at_ending(98)

    ll.insert_values(['hey',344,'bhack','mack','bhang'])

    # a = ll.head
    # a.next.next.next.next.next = Node('blah',a)
    # tupled = ll.detect_loop_floyds_algo()
    # print("length of loop is : {} at {} node".format(tupled[0],tupled[1]))
    # print('LL : ',end ="")
    # ll.print()


    ll.insert_after_by_value(344,430)
    # ll.remove_by_value(344)
    ll.search_node('mack')
    
    
    
    print("3rd node ->",ll.get_nth_node(3))  
    


    # ll.remove_at(2)
    # ll.print()

    ll.insert_at(1,'flags')
    # print("third last element -> ",ll.get_nth_node_from_last(3))
    
    # print("middle element(s) from given ll : ",ll.middle_element())
    # print("430 has been occured at index -> ",occur_of_int(430,ll))
    

    # ll.insert_values(['r','a','d','a','r'])
    # print(ll.check_palindrome())
    
    # ll.swap_nodes(ll.head,ll.head.next.next.next.next.next.next)
    # ll.print()

    # l1 = LinkedList()
    # l1.insert_values([2,3,4,5,6,7])
    # l2 = LinkedList()
    # l2.insert_values([1,3,5,7])
    # intersected_LL = ll.intersection_sorted_LL(l1.head,l2.head)
    # printa(intersected_LL)
    
    