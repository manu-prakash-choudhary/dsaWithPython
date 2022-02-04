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

        
if __name__ == '__main__':
    ll =LinkedList()
    ll.insert_at_begining(900)
    ll.insert_at_begining(89)
    ll.insert_at_begining(34)
    ll.insert_at_ending(98)

    ll.insert_values(['hey',344,'bhack','mack','bhang'])
    ll.insert_after_by_value(344,430)
    # ll.remove_by_value(344)
    # print(ll.search_node('mack'))
    print("3rd node ->",ll.get_nth_node(3))
    ll.print()



    # ll.remove_at(2)
    # ll.print()

    ll.insert_at(1,'flags')
    ll.print()
    ll.delete_list()
    