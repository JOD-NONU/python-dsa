"""
LeetCode 58 - Length of Last Word

Pattern:
Reverse String Traversal

Time Complexity:
O(n)

Space Complexity:
O(1)

Approach:
Traverse the string from the end.
Skip all trailing spaces.
Once the last word starts, count its characters.
Stop when a space is encountered after counting begins.
Return the count.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=0
        for i in range (-1,-len(s)-1,-1):
            if s[i]!=' ':
                k=k+1
            else:
                if k>0 and s[i]==" ":
                    break
        return k