"""
LeetCode 1768 - Merge Strings Alternately

Pattern:
Two Pointers on Strings

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)

Approach:
Traverse both strings simultaneously until the length of the shorter string.
Append one character alternately from each string to the result.
After the traversal, append the remaining characters of the longer string.
Return the final merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s3=""
        if len(word1)>len(word2):
            for i in range (len(word2)):
                s3=s3+word1[i]+word2[i]
            s3=s3+word1[len(word2):]
        else:
            for i in range (len(word1)):
                s3=s3+word1[i]+word2[i]
            s3=s3+word2[len(word1):]
        return s3