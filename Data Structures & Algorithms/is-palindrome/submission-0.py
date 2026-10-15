class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return trimmed_str[::-1] == trimmed_str
        