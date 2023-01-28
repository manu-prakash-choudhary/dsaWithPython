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
        self.root = None

    def get_parent_index(self, index):
        return (index-1)//2
    
    def get_left_child(self,index):
        return 2*index + 1

    def get_right_child(self,index):
        return 2*index + 2