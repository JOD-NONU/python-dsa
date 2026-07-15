"""
LeetCode 283 - Move Zeroes

Pattern:
Two Pointers
Read Pointer + Write Pointer
In-place Swapping

Time Complexity:
O(n)

Space Complexity:
O(1)

Approach:
Use two pointers:
- i -> Read Pointer
- k -> Position of next non-zero element

Traverse the array once.
Whenever a non-zero element is found,
swap it with nums[k] and increment k.

This keeps all non-zero elements in their
original order while moving all zeroes to
the end of the array.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        for i in range (len(nums)):
            if nums[i]!= 0:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
