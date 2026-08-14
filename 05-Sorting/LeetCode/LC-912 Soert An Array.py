'''LeetCode 912 - Sort an Array

Topic:
Sorting(Merge Sort)

Brute Force:
Use simple sorting algorithms such as Bubble Sort, Selection Sort,
or Insertion Sort to sort the array.
These approaches repeatedly compare and rearrange elements until
the entire array becomes sorted.

Time Complexity: O(n²)
Space Complexity: O(1)

Optimal Approach:
Use Merge Sort based on the Divide and Conquer approach.
Divide the array into two halves recursively until every subarray
contains only one element.
A single element is already sorted.
Then merge the sorted left and right halves by comparing their
elements and adding the smaller element to a new result array.
Continue merging the smaller sorted arrays until the complete
array becomes sorted.

Time Complexity: O(n log n)
Space Complexity: O(n)'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            if i<len(left):
                while i<len(left):
                    result.append(left[i])
                    i+=1
            if j<len(right):
                while j<len(right):
                    result.append(right[j])
                    j+=1
            return result
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]
            left=merge_sort(left)
            right=merge_sort(right)
            return merge (left,right)
        return merge_sort(nums)