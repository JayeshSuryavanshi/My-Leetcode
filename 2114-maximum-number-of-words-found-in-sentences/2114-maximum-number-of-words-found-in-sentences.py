class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        _ = []  
        for i in range(len(sentences)):
            _.append(len(sentences[i].split()))
        return max(_)
        
        