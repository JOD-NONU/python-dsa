"""
LeetCode 167 - Two Sum II

Pattern:
Two Pointers 

Brute Force:
For every element, search the remaining part of the array linearly for the required complement.

Time Complexity: O(n²)
Space Complexity: O(1)

Optimal Approach:
Since the array is already sorted, initialize one pointer at the beginning and another at the end
 Compare the sum of both elements with the target. If the sum is greater than the target,
 move the right pointer to decrease the sum. If the sum is smaller than the target,
 move the left pointer to increase the sum. Repeat until the required pair is found.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        m=len(numbers)-1
        while l<m:
            if numbers[l]+numbers[m]>target:
                m=m-1
            elif numbers[l]+numbers[m]<target:
                l=l+1
            else:
                return[l+1,m+1]
                break