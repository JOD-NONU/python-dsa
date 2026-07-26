"""
LeetCode 567 - Permutation in String

Topic:
Sliding Window (Fixed Size) + HashMap

Brute Force:
Generate every substring of length len(s1).
For each substring, calculate its frequency map and compare it with the frequency map of s1.
If both frequency maps are equal, return True.
Otherwise, continue checking all possible substrings.
If no valid permutation is found, return False.

Time Complexity: O((n-m+1) × m)
Space Complexity: O(1)

Optimal Approach:
First, create a frequency map for s1.
Create another frequency map for the first window of size len(s1) in s2.
Compare both maps.
Now slide the window one character at a time.
For every new window:
Add the new character entering the window.
Remove the leftmost character leaving the window.
If the frequency of a character becomes zero, remove it from the map.
Compare both frequency maps.
If both maps become equal at any point, return True.
Otherwise, after checking every window, return False.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        q={}
        p={}
        for i in range (len(s1)):
            if s1[i] not in q:
                q[s1[i]]=0
            q[s1[i]]+=1
        for i in range(len(s1)):
            if i>= len(s2):
                return False
                break
            if s2[i] not in p:
                p[s2[i]]=0
            p[s2[i]]+=1
            if p==q:
                return True
                break
        else:
            for j in range (len(s1),len(s2)):
                if s2[j] not in p:
                    p[s2[j]]=0
                p[s2[j]]+=1
                p[s2[l]]-=1
                if p[s2[l]]==0:
                    p.pop(s2[l])
                if p==q:
                    return True
                    break
                l=l+1
            else:
                return False