'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

'''

# class Node(object):
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
    
#     #returns refrence to the middle node of the list
#     def findMiddle(head):
#         #match step --> 2 pointers
#         #1 pointer is slow
#         #1 pointer is fast

#         #initialize both pointers
#         slow = fast = head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
        
#         return slow


# list1 = Node()
# list2 = Node()

'''
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
'''
# def hashCycle(head):
#     slow = fast = head

#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next

#         if fast == slow:
#             return True
    
#     return False

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# n1.next = n2
# n2.next = n3
# n3.next = n1

# print(f"Cycle detected: {hashCycle(n1)}")  # Output: True

'''
Problem 1: Wild Goose Chase
You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect the clue might be a red herring meant to send you around in circles. Write a function is_circular() that accepts the head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. Otherwise, return False.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#     head = tail = clues
     
#     while tail:
#         tail = tail.next.next
#         head = head.next

#         if tail == head:
#             return True
#     return False

# #Example Usage:
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))
# #Example Output: True

#Mock interview-------------------------
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    #@staticmethod
    def findMiddle(head):
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

# Creating a linked list (non-circular)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node1  # Removed to avoid infinite loop

# Finding the middle node
middle_node = Node.findMiddle(node1)
print(middle_node.value)  # Expected output: 2 (for even length list)


#node_values = Node(1, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))





