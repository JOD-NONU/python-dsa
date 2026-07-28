"""
LeetCode 33 - Search in Rotated Sorted Array

Topic:
Searching (Binary Search)

Brute Force:
Traverse the entire array.
If target is found, return its index.
Otherwise return -1.

Time Complexity: O(n)
Space Complexity: O(1)

Optimal Approach:
At every iteration
one half of the array is always sorted.
Find the middle element.
If middle element is the target
return its index.
Check whether the left half is sorted.
If the left half is sorted,
check whether the target lies inside it.
If yes
discard the right half.
discard the left half.
If the left half is not sorted
the right half must be sorted.
Check whether the target lies inside the right half.
If yes
discard the left half.
discard the right half.
Continue until the target is found or the search space becomes empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid= (r+l)//2
            if nums[mid]== target:
                return mid
                break
            elif nums[l]<=nums[mid]:
                if nums[l]<=target and nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[r]>nums[mid]:
                if nums[r]>=target and nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        else:
            return -1