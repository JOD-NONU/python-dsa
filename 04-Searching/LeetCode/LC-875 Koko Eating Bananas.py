"""
LeetCode 875 - Koko Eating Bananas

Topic:
Binary Search(Binary Search on Answer)

Brute Force:
Try every possible eating speed
from 1 to max(piles).
For every speed,
calculate the total hours required.
Return the first speed
whose required hours are less than or equal to h.

Time Complexity:O(n × max(piles))
Space Complexity:O(1)

Optimal Approach:
Binary Search on Answer
Observation:
The answer always lies between
1 and max(piles)
Minimum speed = 1
Maximum useful speed = largest pile.
For every candidate speed,
calculate the required hours.
If hours <= h,
the speed is valid.
Store it as a possible answer
and search the left half
for a smaller valid speed.
Otherwise,
increase the speed
by searching the right half.

Time Complexity:O(n log(max(piles)))
Space Complexity:O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l=1
        r=max(piles)
        ans=0
        hours=0
        while l<=r:
            mid=(l+r)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans