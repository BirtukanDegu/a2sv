# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev = None
        current = head
        tail = None
        cache = list()
        
        
        while current:    
        
            for _ in range(k):
                if not current: 
                    tail = cache.pop(0) 
                    cache = list() 
                    break
                cache.append(current)
                current = current.next
            
            nxt = current 
        
            while cache:
                current = cache.pop()
                if prev:
                    prev.next = current
                else:
                    head = current
                prev = current
            
            current = nxt 
        
        prev.next = tail 
        
        return head