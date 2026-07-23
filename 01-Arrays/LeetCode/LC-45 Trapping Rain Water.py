"""
LeetCode 42 - Trapping Rain Water

Difficulty: Hard

Topic:
Two Pointers

Brute Force:
For every index, find the maximum height on the left and the maximum height on the right.
The trapped water at that index is:
min(leftMax, rightMax) - currentHeight.

Time Complexity: O(n²)
Space Complexity: O(1)

Better Approach:
Precompute leftMax[] and rightMax[] arrays, then calculate trapped water.

Time Complexity: O(n)
Space Complexity: O(n)

Optimal Approach:
Use Two Pointers with leftMax and rightMax.
Maintain the maximum height seen from both ends.
Always process the side having the smaller maximum because its trapped water is already determined.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        water=0
        c=0
        while l<r:
            if lm < rm:
                l=l+1
                lm=max(lm,height[l])
                c=((lm)-height[l])
                water += max(0, c)
            else:
                r=r-1
                rm=max(height[r],rm)
                c=((rm)-height[r])
                water += max(0, c)
        return water