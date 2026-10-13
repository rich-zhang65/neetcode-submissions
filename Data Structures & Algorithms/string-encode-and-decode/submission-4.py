class Solution:

    def encode(self, strs: List[str]) -> str:
        encodings = []
        for s in strs:
            encodings.append(f"{len(s)}#{s}")
        return "".join(encodings)


    def decode(self, s: str) -> List[str]:
        sol = []

        count_str = ""
        ptr = 0
        while ptr < len(s):
            if s[ptr] == '#':
                count = int(count_str)
                sol.append(s[ptr+1:ptr+count+1])

                ptr = ptr + count + 1
                count_str = ""
            else:
                count_str += s[ptr]
                ptr += 1
        
        return sol

