# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
            
        stack = []
        result = [0] * len(nums)
        for idx in range(len(nums)):
            while stack and (nums[stack[len(stack)-1]] < nums[idx]):
                result[stack.pop()] = nums[idx]
            stack.append(idx)
        return result


