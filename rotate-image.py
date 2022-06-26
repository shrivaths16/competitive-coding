# rotating a matrix by 90 degrees clockwise
# leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
# solution: https://youtu.be/fMSJSS7eO1w

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        
        while l<r:
            for i in range(r-l):
                top, bottom = l, r
                
                #save top left element
                topLeft = matrix[top][l + i]
                
                #bottom left into top left
                matrix[top][l + i] = matrix[bottom-i][l]
                
                #bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                #top right into bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                #top left into top right
                matrix[top+i][r] = topLeft
                
            l+=1
            r-=1
