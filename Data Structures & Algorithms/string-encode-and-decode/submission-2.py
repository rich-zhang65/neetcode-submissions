class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = "".join(list(map(lambda x: 'Ʒ' + x, strs)))
        return encoding

    def decode(self, s: str) -> List[str]:
        decoded = s.split('Ʒ')

        return decoded[1:]

