"""
LeetCode 278 - First Bad Version

Topic:

Searching (Binary Search)

Brute Force:
Start checking versions from 1 to n.
Return the first version for which isBadVersion(version) returns True.

Time Complexity: O(n)
Space Complexity: O(1)

Optimal Approach:
Initialize:
left = 1
right = n
Find the middle version.
If the middle version is good,
the first bad version must be on the right side.
Move:
left = mid + 1
If the middle version is bad,
store it as the current answer and continue searching on the left side
because an earlier bad version may exist.
Move:
right = mid - 1
After the loop finishes,
return the stored answer.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        ans=0
        while l<=r:
            mid=(r+l)//2
            if isBadVersion(mid)==False:
                l=mid+1
            elif isBadVersion(mid)==True:
                ans=mid
                r=mid-1
        return ans