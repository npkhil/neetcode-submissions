class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "|" + s
        return out
    
    def decode(self, s: str) -> List[str]:
        # print(s)
        out = []
        pointer = 0
        length = 0
        while pointer < len(s):
            cur = ""
            while s[pointer] != "|" and length == 0:
                cur += s[pointer]
                pointer += 1
            length = int(cur)
            pointer += 1
            cur = ""
            while length > 0:
                cur += s[pointer]
                length -= 1
                pointer += 1
            out.append(cur)

        return out