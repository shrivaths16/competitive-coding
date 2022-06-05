#replacing elements with the biggest element to the right 
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length=len(arr)
        max=arr[-1]
        
        for i in range(length-2, -1, -1):
            if arr[i]>max:
                temp=max
                max=arr[i]
                arr[i]=temp
            else:
                arr[i]=max
     
        arr[length-1]=-1        
        return arr
