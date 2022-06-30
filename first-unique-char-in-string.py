# to find and return the index of the first unique character in a string
# leetcode: https://leetcode.com/problems/first-unique-character-in-a-string/
# solution video: https://youtu.be/wlRezT0b5MI
class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        
        counter = collections.Counter(s)
        
        for i in range(len(s)):
            if counter.get(s[i]) == 1:
                return i
            
        return -1
