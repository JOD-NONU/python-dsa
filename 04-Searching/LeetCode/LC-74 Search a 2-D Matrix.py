"""
LeetCode 74 - Search a 2D Matrix

Topic:
Searching (Binary Search)

Brute Force:
Traverse every row and every column.
Compare every element with the target.

Time Complexity: O(m × n)
Space Complexity: O(1)


Optimal Approach (Two Binary Searches):
Apply Binary Search on the first element of every row.
Find the row in which the target can possibly exist.
If no such row exists,
return False.
Apply another Binary Search on that row.
If target is found,
return True.
Otherwise,
return False.

Time Complexity:O(log m + log n)
Space Complexity:O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        nums=[]
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid+1
        if r==-1:
            return False
        nums=matrix[r]
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                return True
                break
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        else:
            return False