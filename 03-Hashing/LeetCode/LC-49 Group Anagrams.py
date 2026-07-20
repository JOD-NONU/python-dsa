"""
LeetCode 49 - Group Anagrams

Pattern:
Hashing + Sorting

Time Complexity:
O(n × k log k)

Space Complexity:
O(n × k)

Approach:
For every string, sort its characters.
Use the sorted string as the hash map key.
If the key already exists, append the original string.
Otherwise, create a new group.
Finally, return all groups stored in the hash map.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s="".join(sorted(i))
            if s in d:
                d[s]+=[i]
            else:
                d[s]=[i]
        strs=[]
        for i in d:
            strs+=[d[i]]
        return strs