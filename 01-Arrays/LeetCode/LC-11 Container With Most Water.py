"""
LeetCode 11 - Container With Most Water

Pattern:
Two Pointers (Opposite Direction)

Brute Force:
Consider every possible pair of lines. Calculate the area formed by each pair using
Area = min(height[i], height[j]) × (j - i).
Return the maximum area among all pairs.

Time Complexity: O(n²)
Space Complexity: O(1)

Optimal Approach:
Initialize two pointers, one at the beginning and one at the end of the array. At each step,
calculate the area formed by the two lines and update the maximum area if required. Move the
pointer having the smaller height because moving the taller line cannot increase the area while
the width is decreasing. Continue until both pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        k=len(height)-1
        ans=0
        while l<k:
            if height[l]<height[k]:
                area=height[l]*(k-l)
                l=l+1
            else:
                area=height[k]*(k-l)
                k=k-1
            if area > ans:
                ans=area
        return ans