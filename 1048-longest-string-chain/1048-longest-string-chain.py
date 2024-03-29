class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dictionary = {}
        for w in sorted(words, key=len):
            dictionary[w] = max(dictionary.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dictionary.values())
        