class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        flat_list = [num for subarray in nums for num in subarray]
        counter = Counter(flat_list)
        result  =  [ num for num,freq in counter.items() if freq==len(nums)]
        result.sort()
        return result
        