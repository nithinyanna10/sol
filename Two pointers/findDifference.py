class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = nums1.copy()
        second = nums2.copy()
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                first.remove(nums1[i])
        result.append(list(set(first)))
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                second.remove(nums2[i])
        result.append(list(set(second)))
        return result

        
        
        