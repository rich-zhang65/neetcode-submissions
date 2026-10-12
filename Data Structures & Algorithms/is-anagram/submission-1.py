class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        
        for letter in s:
            letters[ord(letter) - ord('a')] += 1

        for letter in t:
            letters[ord(letter) - ord('a')] -= 1

        return all(count == 0 for count in letters)