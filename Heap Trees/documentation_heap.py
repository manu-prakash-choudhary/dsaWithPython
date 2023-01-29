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
    . Heap can be created with O(N) time.(Proof - https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/)

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

                5) Patient treatment: In a hospital, an emergency patient, or the patient with more injury is treated first. Here the priority is the degree of injury.
                6) Systems concerned with security use heap sort, like the Linux kernel.
                7) Used in graph algorithms such as Dijkstra and A* search algorithms.


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

--------->  Heap Sort:
               It is one of the fastest sorting algorithms with time comoplexity of O(N*logN) and its easy to implement
               Heap sort is an in-place algorithm.
               Its typical implementation is not stable, but can be made stable.
               Typically 2-3 times slower than well-implemented QuickSort.  The reason for slowness is a lack of locality of reference.

            Advantages of heapsort:
               . Efficiency - The time required to perform Heap sort increases logarithmically while other algorithms may grow exponentially slower as the number of items to sort increases. This sorting algorithm is very efficient.
               . Memory Usage - Memory usage is minimal because apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work
               . Simplicity -  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion.

            Disadvantages of Heap Sort:
               . Costly: Heap sort is costly.
               . Unstable: Heat sort is unstable. It might rearrange the relative order.
               . Efficient: Heap Sort are not very efficient when working with highly complex data.

            Applications of HeapSort:
               . Heapsort is mainly used in hybrid algorithms like the IntroSort.
               . Sort a nearly sorted (or K sorted) array
               . k largest(or smallest) elements in an array



--------->  Bionomial Tree: A Binomial Tree of order 0 has 1 node. A Binomial Tree of order k can be constructed by taking two binomial trees of order k-1 and making one the leftmost child of the other.

            - A Binomial Tree of order k the has following properties.
               . It has exactly 2k nodes.
               . It has depth as k.
               . There are exactly kaiCi nodes at depth i for i = 0, 1, . . . , k.
               . The root has degree k and children of the root are themselves Binomial Trees with order k-1, k-2,.. 0 from left to right.

            Example:

               k = 0 (Single Node)

                     o

               k = 1 (2 nodes)
               [We take two k = 0 order Binomial Trees, and
               make one as a child of other]
               o
              /
             o


--------->  Bionomial Heap: A Binomial Heap is a set of Binomial Trees where each Binomial Tree follows the Min Heap property.
                           And there can be at most one Binomial Tree of any degree.

                           Below is an example of Binomial heap with 13(i.e., 1101 in binary) Nodes and 3 binary trees of order 2,3 and 0 order
                           No of bionomial trees in a bionomial heap will be decided by number of ones in the binary of total number of nodes and
                           order of those trees will be given by the places at which the ones occur. For example if N = 13 then binary of 13 will
                           be 1101 and therefore its bionomial heap will be of 3 binomial trees which will be of order 0, 2 and 3 as '1' occur at
                           these places in the binary of 13
                                 ______________________________________
            header[H]----->      |12--------->10------------------->20 |
                                 |_____________________________________|
                                             /  \                 / | \
                                          15    50             70  50  40
                                          |                  / |    |
                                          30               80  85  65
                                                            |
                                                            100
                           A Binomial Heap with 13 nodes. It is a collection of 3
                           Binomial Trees of orders 0, 2, and 3 from left to right.

                           A Binomial Heap with n nodes has the number of Binomial Trees equal to the number of set bits in the binary representation of n.
                           For example, let n be 13, there are 3 set bits in the binary representation of n (00001101), hence 3 Binomial Trees.
                           We can also relate the degree of these Binomial Trees with positions of set bits.
                           With this relation, we can conclude that there are O(Logn) Binomial Trees in a Binomial Heap with 'n' nodes.


--------->  Operations of Binomial Heap:
                  1. The main operation in Binomial Heap is a union(), all other operations mainly use this operation. The union() operation is to combine two Binomial Heaps into one.
                  2. insert(H, k): Inserts a key 'k' to Binomial Heap 'H'. This operation first creates a Binomial Heap with a single key 'k', then calls union on H and the new Binomial heap.
                  3. gettingMin(H): A simple way to getMin() is to traverse the list of the roots of Binomial Trees and return the minimum key. This implementation requires O(Logn) time. It can be optimized to O(1) by maintaining a pointer to the minimum key root.
                  4. extractingMin(H): This operation also uses a union(). We first call getMin() to find the minimum key Binomial Tree, then we remove the node and create a new Binomial Heap by connecting all subtrees of the removed minimum node. Finally, we call union() on H and the newly created Binomial Heap. This operation requires O(Logn) time.
                  5. delete(H): Like Binary Heap, the delete operation first reduces the key to minus infinite, then calls extractingMin().
                  6. decrease key(H): decrease key() is also similar to Binary Heap. We compare the decreased key with its parent and if the parent’s key is more, we swap keys and recur for the parent. We stop when we either reach a node whose parent has a smaller key or we hit the root node. The time complexity of the decrease key() is O(Logn).
---------> Union operation in Binomial Heap:
                  Given two Binomial Heaps H1 and H2, union(H1, H2) creates a single Binomial Heap.

                  . The first step is to simply merge the two Heaps in non-decreasing order of degrees.
                  . After the simple merge, we need to make sure that there is at most one Binomial Tree of any order. To do this, we need to combine Binomial Trees of the same order. We traverse the list of merged roots, we keep track of three-pointers, prev, x, and next-x. There can be the following 4 cases when we traverse the list of roots.
                     —-Case 1: Orders of x and next-x are not the same, we simply move ahead.
                     In the following 3 cases, orders of x and next-x are the same.
                     —-Case 2: If the order of next-next-x is also the same, move ahead.
                     —-Case 3: If the key of x is smaller than or equal to the key of next-x, then make next-x a child of x by linking it with x.
                     —-Case 4: If the key of x is greater, then make x the child of next.
                     
                     refer image (https://media.geeksforgeeks.org/wp-content/uploads/Bionomial_tree_2.png) for better understanding.
'''

from binary_heap import MinHeap

heap_obj = MinHeap(15)   # 15 will be the capacity of the heap
heap_obj.insert(10)
heap_obj.insert(11)
heap_obj.insert(13)
heap_obj.insert(14)
heap_obj.insert(8)
heap_obj.insert(5)
heap_obj.insert(0)
print(heap_obj.storage)
print(heap_obj.remove_min())
print(heap_obj.storage)
main_str = str(heap_obj.storage)
print(main_str)
from drawtree import draw_level_order
draw_level_order(main_str)
# bal line
