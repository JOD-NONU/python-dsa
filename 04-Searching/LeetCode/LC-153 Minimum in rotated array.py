"""
LeetCode 153 - Find Minimum in Rotated Sorted Array

Topic:
Searching (Binary Search)

Brute Force:
Traverse the entire array.
Return the smallest element.

Time Complexity: O(n)
Space Complexity: O(1)

Optimal Approach:
Use Binary Search.
At every iteration,
compare the middle element with the rightmost element.
Case 1:
nums[mid] > nums[right]
Minimum must be in the right half.
Discard the left half.
left = mid + 1
Case 2:
nums[mid] <= nums[right]
The right half is already sorted.
The minimum can still be at mid.
Discard only the right half.
right = mid
Continue until
left == right
That position is the minimum element.
Return nums[left].

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid
            else:
                return nums[l]
                break
