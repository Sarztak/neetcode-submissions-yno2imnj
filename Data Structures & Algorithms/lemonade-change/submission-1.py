class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [0] * 3
        for i in range(len(bills)):
            change = bills[i] - 5
            if change == 0:
                arr[0] += 1
            elif change == 5 and arr[0] > 0:
                arr[0] -= 1
                arr[1] += 1
            else:
                if arr[0] > 0 and arr[1] > 0:
                    arr[0] -= 1 
                    arr[1] -= 1
                    arr[2] += 1
                elif arr[0] >= 3:
                    arr[0] -= 3
                    arr[2] += 1
                else:
                    return False

        return True

        