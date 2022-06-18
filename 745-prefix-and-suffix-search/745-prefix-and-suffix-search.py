class WordFilter:
    def __init__(self, words: List[str]):
        self.wordIndexDict = {}
        for i, word in enumerate(words):
            for suffixStart in range(len(word),-1,-1):
                for prefixEnd in range(len(word)+1):
                    currString = word[suffixStart:]+'#'+word[:prefixEnd]
                    self.wordIndexDict[currString] = i

    def f(self, prefix: str, suffix: str) -> int:
        searchString = suffix+'#'+prefix
        if searchString in self.wordIndexDict:
            return self.wordIndexDict[searchString]
        return -1