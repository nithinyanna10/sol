class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        """
        Do not return anything, modify arr in-place instead.
        """
        n = 0
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == 0:
                n += 1 
                arr.insert(i+1,0)
                arr.pop()
        
        print(arr)
        