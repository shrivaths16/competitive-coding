# To check whether a string is a palindrome or not, by considering only the alphanumeric characters
# leetcode problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
# solution: https://youtu.be/jJXJ16kPFWg
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while l < r and not self.alphaNum(s[l]):
                l += 1    
            while l < r and not self.alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
            
        return True
      
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or #ord returns the ASCII value
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
