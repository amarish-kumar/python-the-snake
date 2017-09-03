"""
	{
		"created_on": "3 Aug 2017",
		"aim": "Creating and reversing singly linked lsit",
		"coded_by": "Rishikesh Agrawani"
	}
"""

class Node(object):
	""" class that defines Node """
	def __init__(self, data):
		self.data = data
		self.next = None

	def show_nodes(self):
		""" method that prints nodes """
		node = self
		while node:
			print node.data
			node = node.next
		print "\n"

	def reverse(self):
		""" method that reverses linked list """
		back, node, forw = None, self, self
		while node:
			forw = node.next
			node.next = back
			back = node
			node = forw
		return back

# point of entry 
if __name__ == "__main__":
	node1 = Node(1)
	node1.next = Node(5)
	node1.next.next = Node(8)
	node1.next.next.next = Node(-67)
	node1.next.next.next.next = Node(0)
	node1.next.next.next.next.next = Node(-5)

	node1.show_nodes()
	node1 = node1.reverse()
	node1.show_nodes()

