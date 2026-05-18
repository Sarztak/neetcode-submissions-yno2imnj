class Solution:
    # instead of using the ascii characters themselves I can just use their numberic
    # representation and then encode those numbers as string separated by a comma
    # then on the other end convert those numbers back to the ascii character
    # for space as well I use a | as delimiter between strings themselves and comma
    # as delimited between the ascii number 
    # so something like 0,0,0|1,123,213
    # the required function are ord to find the ascii number and chr to convert back from number to character

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "Empty"
        ascii_strs = []
        for s in strs:
            s_ascii = ",".join([str(ord(x)) for x in s])
            ascii_strs.append(s_ascii)
        return "|".join(ascii_strs)

    def decode(self, s: str) -> List[str]:
        if s == 'Empty':
            return []
        decoded_strs = []
        for x in s.split('|'):
            og_str = "".join([chr(int(y)) for y in x.split(',') if y])
            decoded_strs.append(og_str)
        return decoded_strs
