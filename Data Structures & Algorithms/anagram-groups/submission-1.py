from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to solve this I will make the sorted string as the key 
        # and the original strings will be put into a list 
        d = defaultdict(list)

        for s in strs:
            if len(s) == 0:
                # I don't know if empty strings are accepted as keys or not
                # but better to be intentional about it
                d[-1].append("") 
            else:
                # also sorted returns a list when a string is passed
                d["".join(sorted(s))].append(s)
        
        # now once this is done I can return the values from the dict
        # the only thing to watch for are empty lists and other things
        return list(d.values())
