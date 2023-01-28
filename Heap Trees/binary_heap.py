
class Node():
    def __init__(self) -> None:
        self.data = None
        self.next = None


'''
'''
class MinHeap():
    def __init__(self, capacity) -> None:
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

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
        self.heapify_up(self.size - 1)

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

    def left_child(self, index):
        left_child_ind = self.get_left_child_index(index)
        return self.storage[left_child_ind]

    def right_child(self, index):
        right_child_ind = self.get_right_child_index(index)
        return self.storage[right_child_ind]

    def remove_min(self):
        if (self.size == 0):
            raise("Heap Already Empty")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return data

    # heapify down iterative approach
    # def heapify_down(self):
    #     index = 0
    #     while (self.has_left_child(index)):
    #         smaller_child_index = self.get_left_child_index(index)
    #         if (self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
    #             smaller_child_index = self.get_right_child_index(index)
    #         if self.storage[index] < self.storage[smaller_child_index]:
    #             break
    #         else:
    #             self.swap(index, smaller_child_index)
    #         index = smaller_child_index

    # Recursive approach of heapify down
    def heapify_down(self, index):
        smaller_child_index = index
        if (self.has_left_child(index) and self.storage[smaller_child_index] > self.left_child(index)):
            smaller_child_index = self.get_left_child_index(index)
        if (self.has_right_child(index) and self.storage[smaller_child_index] > self.right_child(index)):
            smaller_child_index = self.get_right_child_index(index)
        if smaller_child_index != index:
            self.swap(smaller_child_index, index)
            self.heapify_down(smaller_child_index)
