#rotating an array k number of times
#leetcode link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        left=0
        right=len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1 
        
        left=k
        right=len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1 
        
        left=0
        right=k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1 
