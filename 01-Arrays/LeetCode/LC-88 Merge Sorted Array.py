"""
LeetCode 88 - Merge Sorted Array

Pattern:
Reverse Two Pointers
In-place Merge

Time Complexity:
O(m+n)

Space Complexity:
O(1)

Approach:
Use three pointers:
- k -> Last valid element of nums1
- l -> Last element of nums2
- z -> Last index of nums1

Compare elements from the end.
Place the larger element at nums1[z].
Move the corresponding pointer backward.

If nums1 gets exhausted first,
copy the remaining elements of nums2.

If nums2 gets exhausted first,
no extra work is required because
the remaining elements of nums1
are already in their correct positions.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=m-1
        l=n-1
        z=len(nums1)
        while l>-1:
            if l>=0 and k== -1:
                for i in range(l+1):
                    nums1[i]=nums2[i]
                l=-1
            elif nums1[k]>nums2[l]:
                nums1[z-1]=nums1[k]
                z=z-1
                k=k-1
            else:
                nums1[z-1]=nums2[l]
                l=l-1
                z=z-1