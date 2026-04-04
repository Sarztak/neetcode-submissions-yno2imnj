class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        max_len = 1 
        curr_len = 1
        if arr[1] > arr[0]:
            sign = -1
        elif arr[1] < arr[0]:
            sign = 1
        else:
            sign = 0

        for i in range(1, n): # the length is till position i
            if arr[i] > arr[i - 1] and sign < 0:
                curr_len += 1
                sign = 1
                max_len = max(max_len, curr_len)
            elif arr[i] < arr[i - 1] and sign > 0:
                curr_len += 1
                sign = -1
                max_len = max(max_len, curr_len)
            elif arr[i] == arr[i - 1]:
                curr_len = 1
                if i < n - 1:
                    if arr[i + 1] > arr[i]:
                        sign = -1
                    elif arr[i + 1] < arr[i]:
                        sign = 1
                    else:
                        sign = 0
                max_len = max(max_len, curr_len)
            else:
                curr_len = 2
                max_len = max(max_len, curr_len)
        
        return max_len
            

