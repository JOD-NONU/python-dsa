"""
LeetCode 344 - Reverse String

Pattern:
Two Pointers

Time Complexity:
O(n)

Space Complexity:
O(1)

Approach:
Initialize two pointers at the beginning and end of the character array.
Swap the characters at both pointers.
Move the left pointer forward and the right pointer backward.
Continue until the pointers meet or cross.
The string is reversed in-place without using any extra space.
"""
def reverseString(self, s: List[str]) -> None:
        l=0
        k=len(s)-1
        while l<=k:
            s[l],s[k]=s[k],s[l]
            k=k-1
            l=l+1
        return s