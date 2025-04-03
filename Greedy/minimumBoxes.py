class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apples = sum(apple)
        count = 0
        for i in range(len(capacity)):
            apples = apples-capacity[i]
            count+=1
            if apples <= 0 :
                return count
        
        return -1