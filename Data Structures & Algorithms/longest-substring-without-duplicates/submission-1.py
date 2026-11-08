class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        curr_len = 0
        seen = defaultdict(int)

        while right < len(s):
            seen[s[right]] += 1
            curr_len += 1
            
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
                curr_len -= 1
                
            ans = max(ans, curr_len)
            right += 1

        return ans
