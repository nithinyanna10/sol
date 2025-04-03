class Solution:
    def splitNum(self, num: int) -> int:
        arr =  [int(digit) for digit in str(num)]
        arr.sort()
        arr_1 = arr[::2]
        arr_2 = arr[1::2]
        num_str1 = ''.join(map(str, arr_1))
        num_str2 = ''.join(map(str, arr_2))
        return int(num_str1)+int(num_str2)