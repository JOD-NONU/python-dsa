"""
LeetCode 383 - Ransom Note

Pattern:
Hashing (Frequency Count)

Time Complexity:
O(m + n)

Space Complexity:
O(m)

Approach:
Create a frequency map of all characters in the magazine.
Traverse the ransomNote string.
For each character, check whether it exists in the hash map
and whether its frequency is greater than zero.
If not, return False.
Otherwise, decrease its frequency.
If all characters are matched successfully, return True.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in ransomNote:
            if j not in d or d[j]<=0:
                return False
                break   
            else:
                d[j]-=1
        else:
            return True