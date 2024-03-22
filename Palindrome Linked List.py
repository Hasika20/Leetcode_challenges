# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list=[]
        while head!=None:
            list.append(head.val)
            head=head.next
        if list==list[::-1]:
            return True
        else:
            return False
            
        