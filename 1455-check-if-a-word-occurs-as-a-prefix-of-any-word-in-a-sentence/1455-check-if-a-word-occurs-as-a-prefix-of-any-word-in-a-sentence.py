class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = sentence.split()
        for word in res:
            if word.startswith(searchWord):
                return res.index(word) + 1
        return -1
