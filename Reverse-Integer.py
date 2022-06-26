# reversing an integer and checking whether the reversed integer is within the 32 bit range
# leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
# solution: https://youtu.be/HAgLH58IgJQ

class Solution:
    def reverse(self, x: int) -> int:
        res=0
        MIN = -2147483648
        MAX = 2147483647
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            
            if (res > MAX // 10 or
                res == MAX // 10 and digit >= MAX%10):
                return 0
            
            if (res < MIN // 10 or
                res == MIN // 10 and digit <= MIN%10):
                return 0
            res = (res*10) + digit
            
        return res
