"""
LeetCode 217 - Contains Duplicate

Pattern:
Hashing

Time Complexity:
O(n)

Space Complexity:
O(n)

Approach:
Traverse the array once.
Store each element in a hash map.
If the current element is already present in the hash map,
return True immediately.
Otherwise, insert it into the hash map.
If the traversal completes without finding any duplicate,
return False.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                return True
                break
        else:
           return False