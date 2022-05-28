# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        n = len(res)
        return max(res[i] + res[n-i-1] for i in range(n//2))
    
#         ans=[]
#         while head:
#             ans.append(head.val)
#             head=head.next
            
#         a=[]
#         for i in range(len(ans)):
#             a.append(ans[i]+ans[len(ans)-i-1])
#         return max(a)

