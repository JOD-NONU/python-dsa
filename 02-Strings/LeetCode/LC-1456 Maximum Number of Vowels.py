"""
LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length

Topic:
Sliding Window (Fixed Size)

Brute Force:
Generate every substring of length k.
Count vowels in each substring separately.
Return the maximum count.

Time Complexity: O(n*k)
Space Complexity: O(1)

Optimal Approach:
Use a fixed-size sliding window.
Count vowels in the first window.
While sliding the window, remove the leftmost character 
if it is a vowel and add the new character if it is a vowel.
Update the maximum vowel count after every slide.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        ans=0
        for i in range(k):
            if s[i] in "aeiou":
                count=count+1
        ans=count
        for j in range(k,len(s)):
            if s[j-k] in "aeiou":
                count=count-1
            if s[j] in "aeiou":
                count=count+1
            if count>ans:
                ans=count
        return ans