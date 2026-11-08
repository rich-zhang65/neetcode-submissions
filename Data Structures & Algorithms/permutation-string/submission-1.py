class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        counts = [0] * 26

        for s in s1:
            counts[ord(s) - ord('a')] += 1

        for right in range(len(s2)):
            counts[ord(s2[right]) - ord('a')] -= 1

            if right < len(s1) - 1:
                continue

            if all(c == 0 for c in counts):
                return True

            counts[ord(s2[left]) - ord('a')] += 1
            left += 1

        return False
