"""
LeetCode 26 - Remove Duplicate From Sorted Array

Pattern:
Two Pointers

Time Complexity:
O(n)

Space Complexity:
O(1)

Approach:
Use two pointers:
- i -> Read Pointer
- k -> Write Pointer

Traverse the array once.
If current element is not equal to previous element,
copy it to index k and increment k.

Return k.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range (1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
        