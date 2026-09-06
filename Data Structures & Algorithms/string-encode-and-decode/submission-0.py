class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)).zfill(3) + s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = int(s[i: i + 3])
            string = s[i + 3: i + 3 + length]
            res.append(string)
            i += 3 + length
        return res