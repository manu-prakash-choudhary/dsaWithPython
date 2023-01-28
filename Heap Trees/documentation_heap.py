# https://www.geeksforgeeks.org/heap-data-structure/
'''
Generally, Heaps can be of two types:
    Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it's children.
            --> The same property must be recursively true for all sub-trees in that Binary Tree.
    Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it's children. 
            --> The same property must be recursively true for all sub-trees in that Binary Tree.

----> Operations of Heap Data Structure:
            1. Heapify: a process of creating a heap from an array.
            2. Insertion: process to insert an element in existing heap time complexity O(log N).
            3. Deletion: deleting the top element of the heap or the highest priority element, and then 
               organizing the heap and returning the element with time complexity O(log N).
            4. Peek: to check or find the most prior element in the heap, (max or min element for max and min heap).

----> Application of Heap Data Structure:
        Heap is used to construct a priority queue.
        Heap sort is one of the fastest sorting algorithms with time complexity of O(N* log(N), and it's easy to implement.
        Realt time application : Systems concerned with security use heap sort, like the Linux kernel.

----> Advantages of Heap Data Structure:
    . Less time complexity, for inserting or deleting an element in the heap the time complexity is just O(log N).
    . It helps to find the minimum number and greatest number.
    . To just peek at the most prior element the time complexity is constant O(1).
    . Can be implemented using an array, it doesn't need any extra space for pointer.
    . A binary heap is a balanced binary tree, and easy to implement.
    . Heap can be created with O(N) time.

. Heap is analmost complete Binary tree.

----> Disadvantages of Heap Data Structure:

    . The time complexity for searching an element in Heap is O(N).
    . To find a successor or predecessor of an element, the heap takes O(N) time, whereas BST takes only O(log N) time.
    . To print all elements of the heap in sorted order time complexity is O(N*log N), whereas, for BST, it takes only O(N) time.
    . Memory management is more complex in heap memory because it is used globally. Heap memory is divided into two parts-old
      generations and the young generation etc. at java garbage collection.

      
. For any ith node
			Arr[i-1] / 2 represent its parent node
			Arr[2*i + 1] represents its left child
			Arr[2*i + 2] represents its right child

                        
                        
                        
-------->   Applications of Heaps:

                1) Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.
                2) Priority Queue: Priority queues can be efficiently implemented using Binary Heap because it supports
                   insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time. Binomial Heap and
                   Fibonacci Heap are variations of Binary Heap. These variations perform union also efficiently.
                3) Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra's Shortest Path and
                   Prim's Minimum Spanning Tree.
                4) Many problems can be efficiently solved using Heaps. See following for example.
                        a) K'th Largest Element in an array.
                        b) Sort an almost sorted array
                        c) Merge K Sorted Arrays.


--------->  Operations on Min Heap:

                1) get_min(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).

                2) extract_min(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Logn) as this operation
                   needs to maintain the heap property (by calling heapify()) after removing root.

                3) decrease_key(): Decreases value of key. The time complexity of this operation is O(Logn). If the decreases key value of
                   a node is greater than the parent of the node, then we don't need to do anything. Otherwise, we need to traverse up to
                   fix the violated heap property.

                4) insert(): Inserting a new key takes O(Logn) time. We add a new key at the end of the tree. IF new key is greater than
                   its parent, then we don't need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

                5) delete(): Deleting a key also takes O(Logn) time. We replace the key to be deleted with minum infinite by calling
                   decreaseKey(). After decreaseKey(), the minus infinite value must reach root, so we call extractMin() to remove the key.


--------->  Heapify_UP method:
                  In this method we will do the following
                     1) take the last element of the heap.
                     2) we will compare it with its parent node 
                     3) we will swap the element if parent node is greater than current element and we will repeat step 2 and 3 as long as it satifies 
                        the condition and parent node exists
                     4) whenever condition gets violated or parent node does not exist then we will stop our heapify method, which will mean that heapification 
                        has been done.

'''

import binary_heap

print(binary_heap.create_heap())