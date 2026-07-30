"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array

Topic:
Searching (Binary Search)

Brute Force:

Traverse the entire array.
Store the first occurrence of the target.
Continue traversing and keep updating the last occurrence.
Return both indices.

Time Complexity: O(n)
Space Complexity: O(1)

Optimal Approach:
Perform Binary Search twice.
First Binary Search:
Search for the first occurrence.
Whenever the target is found,
store its index,
but continue searching towards the left half.
This guarantees the leftmost occurrence.
Second Binary Search:
Search for the last occurrence.
Whenever the target is found,
store its index,
but continue searching towards the right half.
This guarantees the rightmost occurrence.
In last:
return [first, last].
If the target is never found,
return [-1, -1].

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        first=-1
        last=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                first=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                last=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        if first==-1 and last==-1:
            return [-1,-1]
        else:
            return[first,last]
