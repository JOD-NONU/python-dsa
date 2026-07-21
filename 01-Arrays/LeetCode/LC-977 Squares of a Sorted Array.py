"""
LeetCode 977 - Squares of a Sorted Array

Pattern:
Two Pointers (Opposite Direction)

Brute Force:
Square every element of the array and then sort the array in non-decreasing order.

Time Complexity: O(n log n)
Space Complexity: O(1) Auxiliary

Optimal Approach:
Use two pointers, one at the beginning and one at the end of the sorted array.
Since the largest square will always come from either the leftmost negative
number or the rightmost positive number, compare their squares and place the larger 
square at the last available position of a new array. Move the corresponding pointer inward 
and continue filling the new array from right to left until all elements are processed.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newarr=[0]*len(nums)
        l=0
        k=len(nums)-1
        n=len(newarr)-1
        while n>=0:
            left = nums[l] * nums[l]
            right = nums[k] * nums[k]
            if left>right:
                newarr[n]=nums[l]**2
                l=l+1
                n=n-1
            else:
                newarr[n]=nums[k]**2
                k=k-1
                n=n-1
        return newarr