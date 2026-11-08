class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        most_freq_len = 0
        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1
            most_freq_len = max(most_freq_len, seen[s[right]])

            while (right - left + 1) > most_freq_len + k:
                seen[s[left]] -= 1
                left += 1
                most_freq_len = max(most_freq_len, seen[s[right]])

            ans = max(ans, right - left + 1)

        return ans
        