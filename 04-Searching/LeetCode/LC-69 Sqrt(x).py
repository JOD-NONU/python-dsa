"""
LeetCode 69 - Sqrt(x)

Topic:
Searching (Binary Search)

Brute Force:
Start from 0 and keep checking i*i.
Continue until i*i becomes greater than x.
The previous value of i is the floor square root.

Time Complexity: O(√x)
Space Complexity: O(1)

Optimal Approach:

The square root always lies between 0 and x.
Initialize:
left = 0
right = x
Find the middle value.
If mid² is equal to x,
return mid.
If mid² is smaller than x,
search in the right half.
If mid² is greater than x,
search in the left half.
If the exact square root is not found,
the loop terminates with right pointing to the largest number whose square is less than x.
Return right.

Time Complexity: O(log x)
Space Complexity: O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            mid=(l+r)//2
            if mid*mid<x:
                l=mid+1
            elif mid*mid>x:
                r=mid-1
            else:
                return mid
                break
        else:
            return r