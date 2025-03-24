class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count  = 0
        window_sum = sum(arr[:k])  
        if window_sum // k >= threshold:
            count += 1
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]  
            if window_sum // k >= threshold:
                count += 1
                
        return count
    
        