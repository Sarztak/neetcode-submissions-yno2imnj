class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # take a hint from the output, and focus on the output
        # what we want is length not the substring so instead of 
        # trying to find the substring, we can use pointers to find
        # the length. All this is easier said than done. But still
        # we must think

        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        