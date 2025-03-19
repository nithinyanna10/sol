class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors.append(colors[0])
        colors.append(colors[1])
        count = 0 
        arr = []
        for i in range(len(colors)-2):
            arr.append(colors[i:i+3])
            if colors[i:i+3] == [0,1,0] or colors[i:i+3] == [1, 0, 1]:
                count+=1 
        print(arr)
        return count
        

        