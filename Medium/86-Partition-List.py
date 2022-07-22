# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # create linkedList for each case
        less_node = ListNode()
        great_eq_node = ListNode()
        
        curr_node = head
        less = less_node
        greater = great_eq_node
        
        while curr_node:           
            if curr_node.val < x:
                # add to less list
                less.next = curr_node
                less = less.next
            else:
                # add to geater/equal list
                greater.next = curr_node
                greater = greater.next
            
            curr_node = curr_node.next
        
        # end of less is greater/equal
        less.next = great_eq_node.next
        # remove next. e.g. example 1: 5->2 while 2->4->3->5->5->etc. ==> 5.next=None
        greater.next = None
        
        return less_node.next