class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""

        left = 0
        to_include = len(t)
        counts = defaultdict(int)

        min_len = float('inf')
        start = 0

        for letter in t:
            counts[ord(letter) - ord('a')] += 1

        for right in range(len(s)):
            right_key = ord(s[right]) - ord('a')

            counts[right_key] -= 1
            if counts[right_key] >= 0:
                to_include -= 1

            while to_include == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_key = ord(s[left]) - ord('a')
                counts[left_key] += 1
                left += 1

                if counts[left_key] > 0:
                    to_include += 1

        return "" if min_len == float('inf') else s[start:start+min_len]
