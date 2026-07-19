"""
LeetCode 1 - Two Sum

Pattern:
Hashing

Time Complexity:
O(n)

Space Complexity:
O(n)

Approach:
Traverse the array once.
For each element, calculate the required complement
(target - current element).
Check if the complement already exists in the hash map.
If it exists, return the stored index and the current index.
Otherwise, store the current element with its index.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range (len(nums)):
            diff= target-nums[i]
            if diff in s:
                j=s[diff]
                return[i,j]
                break
            else:
                s[nums[i]]=i