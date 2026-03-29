class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            l = len(s)
            if l < 10:
                prefix = f'00{l}'
            elif l < 100:
                prefix = f'0{l}'
            else:
                prefix = str(l)
            encoded_string += f'{prefix}{s}'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        while len(s) > 0:
            l = int(s[:3])
            decoded_string.append(s[3:3+l])
            s = s[3+l:]
        return decoded_string

