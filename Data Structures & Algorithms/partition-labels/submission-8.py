class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # get the start and end points of each letter
        letters = set(s)
        n = len(s)
        pos_dict = {c:[n + 1, -1] for c in letters} # set some limit for start, end to compare at start

        for i in range(n):
            start, end = pos_dict[s[i]]
            pos_dict[s[i]] = [min(start, i), max(end, i)]

        # now I have the minimum and the maximum position and the problem reduces to merging the windows
        intervals = list(pos_dict.values())

        # sort the windows
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(intervals)
        ans = [] 

        start, end = intervals[0]
        i = 1
        while i < len(intervals):
            if end < intervals[i][0]: # there means there is no over lap
                ans.append(end - start + 1)
                start = intervals[i][0] # update the start value
            end = max(end, intervals[i][1])
            i += 1

        ans.append(end - start + 1)        
        return ans


