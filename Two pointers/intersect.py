class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        small = []
        large = []
        result = []
        if len(nums1) < len(nums2):
            small = nums1
            large= nums2
        else : 
            small = nums2
            large = nums1
        for i in range(len(small)):
            if small[i] in large:
                result.append(small[i])
                large.remove(small[i])
        return result 
        
        