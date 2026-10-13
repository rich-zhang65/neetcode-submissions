class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = self.processLetters(word)
            groups[key].append(word)
                
        return list(groups.values())

    def processLetters(self, word: str):
        letters = [0] * 26

        for letter in word:
            letters[ord(letter) - ord('a')] += 1

        return tuple(letters)