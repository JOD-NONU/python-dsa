"""
LeetCode 3 - Longest Substring Without Repeating Characters

Topic:
Sliding Window (Variable Size)

Brute Force:
Generate every possible substring and check whether all characters are unique.
Keep track of the maximum valid substring length.

Time Complexity: O(n²)
Space Complexity: O(1)

Optimal Approach:
Use a variable-size sliding window with two pointers.
Expand the window by moving the right pointer.
If a duplicate character appears, shrink the window from the left until the duplicate is removed.
Keep updating the maximum window length.

Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""
def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        ans=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left=left+1
            seen.add(s[i])
            ans=max(ans,i-left+1)
        return ans