def create_heap():
    return 'result'

class Node():
    def __init__(self) -> None:
        self.data = None
        self.next = None

class MinHeap():
    def __init__(self, capacity) -> None:
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index):
        return (index-1)//2
    
    def get_left_child(self, index):
        return 2*index + 1

    def get_right_child(self, index):
        return 2*index + 2

    def has_parent(self, index):
        return self.get_parent_index(index)>=0

    def has_left_child(self, index):
        return self.get_left_child < self.size
    
    def has_right_child(self, index):
        return self.get_right_child(index) < self.size
    
    def is_full(self, index):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        if(self.is_full()):
            raise("Heap is full")
        self.storage[self.size] = data
        self.size += 1
        self.heapify_up(self.size -1)
                       
    def parent(self, index):
        if (self.has_parent(index)):
            return self.storage[self.get_parent_index(index)]
        raise("Parent does not exist")

    def heapify_up(self, index):
        if (self.has_parent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.get_parent_index(index), index)
            self.heapify_up(self.get_parent_index(index))

    #  Non Recursive Heapify method
    # def heapify_up(self):
    #     index = self.size - 1
    #     while (self.has_parent(index) and self.parent(index) > self.storage[index]):
    #         self.swap(self.get_parent_index(index), index)
    #         index = self.get_parent_index(index)

