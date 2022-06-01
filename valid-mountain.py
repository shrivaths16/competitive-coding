class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False
        i=0
        while i < length-1 and arr[i+1] > arr[i]:
            i+=1
        
        if i==0 or i==length-1:
            return False
        
        while i < length-1 and arr[i+1] < arr[i]:
            i+=1
            
        if i==length-1:
            return True
        
        return False
