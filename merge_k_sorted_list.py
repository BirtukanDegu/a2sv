# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for ll in lists:
            while ll:
                array.append(ll.val)
                ll = ll.next
        array.sort()
        if array != []:
            self.head = ListNode()
            self.current = self.head
            for number in array:
                self.current.next = ListNode(number)
                self.current = self.current.next
            return self.head.next
        else:
            return 
