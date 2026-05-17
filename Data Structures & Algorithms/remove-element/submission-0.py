class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t = []
        for n in nums:
            if n != val:
                t.append(n)
        
        k = len(t) # these are elements which are not val
        nums[:k] = t

        return k