"""
LeetCode 704 - Binary Search

Topic:

Searching (Binary Search)

Brute Force:
Traverse the array from left to right and compare every element with
the target. If the target is found, return its index.
Otherwise, after traversing the entire array, return -1.

Time Complexity: O(n)
Space Complexity: O(1)

Optimal Approach:
Initialize two pointers:
left = 0
right = len(nums)-1
Find the middle element.
If the middle element is equal to the target,
return its index.
If the target is greater than the middle element,
discard the left half by moving the left pointer.
If the target is smaller than the middle element,
discard the right half by moving the right pointer.
Repeat until the target is found or the search space becomes empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        d=True
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
                break
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        else:
            return -1