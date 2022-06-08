# problem is to find all the elements that are not present in an array in the range of [1,n] where n is the size of the array
# leetcode link: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        result=[]
        
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        
        for i,n in enumerate(nums):
            if n > 0:
                result.append(i+1)
        
        return result
