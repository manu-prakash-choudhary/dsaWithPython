# LinkedList Implementation with a que

'''types 
        Singular ,doubly or circular linked lists
    topics 
        Insertion, deletion,reversal,searching,nth node from last, delete a particular key or at particular position  '''

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

    def insert_after_by_value(self,value):
        pass
    def remove_by_value(self,value):
        pass


if __name__ == '__main__':
    ll =LinkedList()
    ll.insert_at_begining(900)
    ll.insert_at_begining(89)
    ll.insert_at_begining(34)
    ll.insert_at_ending(98)
    ll.print()
    ll.get_length()

    ll.insert_values(['hey',344,'bhack','mack','bhang'])
    ll.print()

    ll.remove_at(2)
    ll.print()

    ll.insert_at(1,'flags')
    ll.print()
