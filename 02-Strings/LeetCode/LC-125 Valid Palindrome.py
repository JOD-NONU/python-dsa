"""
LeetCode 125 - Valid Palindrome

Pattern:
Two Pointers

Time Complexity:
O(n)

Space Complexity:
O(1)

Approach:
Initialize two pointers at the beginning and end of the string.
Skip all non-alphanumeric characters from both sides.
Convert valid characters to lowercase before comparison.
If the characters do not match, return False.
Otherwise, move both pointers towards the center.
If the traversal completes without any mismatch, return True.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        k=len(s)-1
        p=True
        while k>=l:
            if s[l].isalnum() and s[k].isalnum():
                if s[l].lower()!=s[k].lower():
                    p=False
                    return False
                    break
                k=k-1
                l=l+1
            elif s[k].isalnum()==False:
                k=k-1
            elif s[l].isalnum()==False:
                l=l+1
        if p== True:
            return True