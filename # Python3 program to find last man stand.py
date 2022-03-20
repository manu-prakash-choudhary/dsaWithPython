# Python3 program to find last man standing

# /* structure for a node in circular
# linked list */
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None

# /* Function to find the only person left
# after one in every m-th node is killed
# in a circle of n nodes */
def getJosephusPosition(m, n):

	# Create a circular linked list of
	# size N.
	head = Node(1)
	prev = head
	for i in range(2, n + 1):
		prev.next = Node(i)
		prev = prev.next
	prev.next = head # Connect last
					#node to first

	#/* while only one node is left in the
	#linked list*/
	ptr1 = head
	ptr2 = head
	while (ptr1.next != ptr1):
		# Find m-th node
		count = 1
		while (count != m):
			ptr2 = ptr1
			ptr1 = ptr1.next
			count += 1

		# /* Remove the m-th node */
		ptr2.next = ptr1.next
		# free(ptr1)
		ptr1 = ptr2.next

	print("Last person left standing (Josephus Position) is ", ptr1.data)

# /* Driver program to test above functions */
if __name__ == '__main__':
	n = 4
	m = 2
	getJosephusPosition(m, n)

# This code is contributed by mohit kumar 29
