class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        if arr[0] == arr[1]:
            c, m = 1, 1 # c track current length and m track the global max length
        else:
            c, m = 2, 2
        

        for i in range(2, n):
            if arr[i - 2] < arr[i - 1] and arr[i - 1] > arr[i]:
                c += 1; m = max(m, c)
            elif arr[i - 2] > arr[i - 1] and arr[i - 1] < arr[i]:
                c += 1; m = max(m, c)
            elif arr[i - 2] == arr[i - 1] and arr[i - 1] != arr[i]:
                c = 2; m = max(m, c)
            elif arr[i - i] == arr[i]:
                c = 1; m = max(m, c)
            else:
                c = 2; m = max(m, c)

        return m
                
