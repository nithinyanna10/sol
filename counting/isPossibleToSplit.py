class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return not any(freq > 2 for freq in count.values())

        