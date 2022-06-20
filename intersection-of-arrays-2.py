#generating another array that contains the common elements(how many ever times it repeats in both) in the 2 input arrays
#leetcode problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2) 
        i,j=0,0 
        result=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:   
                j+=1
            else:
                result.append(nums1[i])
                i+=1
                j+=1
        return result
