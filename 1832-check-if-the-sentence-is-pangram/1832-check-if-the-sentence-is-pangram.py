class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = len(Counter(sentence))
        if c < 26:
            return False
        return True