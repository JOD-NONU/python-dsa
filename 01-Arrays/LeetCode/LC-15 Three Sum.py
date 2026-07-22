"""
LeetCode 15 - 3Sum

Topic:
Sorting, Two Pointers

Brute Force:
Check every possible triplet using three nested loops.
If the sum of the triplet equals 0, store it while avoiding duplicates.

Time Complexity: O(n³)
Space Complexity: O(1)

Optimal Approach:
Sort the array first. Fix one element using a loop.
Then use Two Pointers (left and right) to find the remaining two elements.
If the sum is greater than 0, move the right pointer.
If the sum is less than 0, move the left pointer.
If the sum is 0, store the triplet and skip duplicates.

Time Complexity: O(n²)
Space Complexity: O(1) (excluding output array)
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i=0
        k=len(nums)-1
        nums.sort()
        r=1
        new=[]
        for i in range (len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                i=i+1
                continue
            r=i+1
            k=len(nums)-1
            while r<k:
                if nums[i]+nums[k]+nums[r]>0:
                    k=k-1
                elif nums[i]+nums[k]+nums[r]<0:
                    r=r+1
                else:
                    new.append([nums[i],nums[r],nums[k]])
                    k=k-1
                    r=r+1
                    while r < k and nums[r] == nums[r-1]:
                        r += 1
                    while r < k and nums[k] == nums[k+1]:
                        k -= 1
        return new