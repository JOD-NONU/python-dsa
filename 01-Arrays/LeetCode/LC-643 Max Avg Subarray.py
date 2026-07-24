"""
LeetCode 643 - Maximum Average Subarray I

Topic:
Sliding Window (Fixed Size)

Brute Force:
Calculate the sum of every subarray of size k using nested loops.
Keep track of the maximum sum and divide it by k at the end.

Time Complexity: O(n*k)
Space Complexity: O(1)

Optimal Approach:
Calculate the sum of the first window of size k.
Slide the window by removing the leftmost element and adding the next element.
Update the maximum window sum during each slide.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win=0
        avg=0
        for i in range(k):
            win=win+(nums[i]/k)
        avg=win
        for j in range(k,len(nums)):
            win=win-(nums[j-k]/k)
            win=win+(nums[j]/k)
            if win>avg:
                avg=win
        return avg