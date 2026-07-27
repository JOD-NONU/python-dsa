"""
LeetCode 35 - Search Insert Position

Topic:
Searching (Binary Search)

Brute Force:
Traverse the array from left to right.
If the current element is greater than or equal to the target,
return its index.
If the traversal completes and the target is still not found,
return the length of the array.

Time Complexity: O(n)
Space Complexity: O(1)

Optimal Approach:
Initialize two pointers:
left = 0
right = len(nums)-1
Find the middle element.
If nums[mid] == target,
return mid.
If target is greater than nums[mid],
search in the right half.
If target is smaller than nums[mid],
search in the left half.
If the target is not found,
the loop ends with left pointing to the correct insertion position.
Return left.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                return mid
                break
        else:
            return l