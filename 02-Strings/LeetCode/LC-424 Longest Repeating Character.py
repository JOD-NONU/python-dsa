"""
LeetCode 424 - Longest Repeating Character Replacement

Topic:
Sliding Window (Variable Size) + HashMap

Brute Force:

Generate every possible substring.
For every substring, calculate the frequency of each character.
Find the maximum frequency character and calculate the number of replacements required.
If replacements are less than or equal to k, update the maximum answer.

Time Complexity: O(n² × 26)
Space Complexity: O(1)

Optimal Approach:

Use a variable-size sliding window with two pointers.
Store the frequency of characters using a HashMap.
Maintain the maximum frequency of any character inside the current window.
If (Window Length - Maximum Frequency) > k
shrink the window from the left until it becomes valid again.
Keep updating the maximum valid window length throughout the traversal.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        seen = {}
        maxfreq = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 0
            seen[s[i]] += 1
            maxfreq = max(maxfreq, seen[s[i]])
            if i - l + 1 - maxfreq <= k:
                r = i - l + 1
                ans = max(ans, r)
            else:
                while i - l + 1 - maxfreq > k:
                    seen[s[l]] -= 1
                    l = l + 1
                r = i - l + 1
                ans = max(ans, r)
        return ans