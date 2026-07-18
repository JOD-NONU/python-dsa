"""
LeetCode 242 - Valid Anagram

Pattern:
Hashing (Frequency Count)

Time Complexity:
O(n)

Space Complexity:
O(n)

Approach:
Check if both strings have equal length.
Create a hash map to count the frequency of characters in the first string.
Traverse the second string.
If a character is missing or its frequency becomes zero, return False.
Otherwise, decrease its frequency by one.
If all characters are matched successfully, return True.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        flag=False
        if len(s)==len(t):
            for i in s:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            for j in t:
                if j not in d or d[j] ==0:
                    flag=True
                    break
                else:
                    d[j]-=1
            if flag==True:
                return False
            else:
                return True
        else:
            return False