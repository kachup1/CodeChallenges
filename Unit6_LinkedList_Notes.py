

'''
https://leetcode.com/problems/remove-linked-list-elements/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         dummyHead.next = head

#         prev, curr = dummyHead, head

#         while curr:
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr.next
#             curr = curr.next
#         return dummyHead.next
    
'''
LRU Cache
https://leetcode.com/problems/lru-cache/description/
'''