# converting a string to an integer, ignoring other characters and whitespcaces
# leetcode problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
# solution: https://youtu.be/zwZXiutgrUE
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2147483647
        MIN = -2147483648
        i = 0
        sign = 1
        res = 0
        #whitespaces
        while i<len(s) and s[i] == " ":
            i += 1
        
        #checking for +/-
        if i<len(s) and s[i] == '-':
            i += 1
            sign = -1
        elif i<len(s) and s[i] == '+':
            i += 1
            
        #check 0-9
        checker = set('0123456789')
        while i<len(s) and s[i] in checker:
            if res > MAX // 10 or (res == MAX//10 and int(s[i]) > 7):
                return MAX if sign == 1 else MIN
            res = res*10 + int(s[i])
            i += 1
        
        return res*sign
