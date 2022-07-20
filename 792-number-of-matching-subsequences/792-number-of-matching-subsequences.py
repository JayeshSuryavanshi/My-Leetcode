class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i =0
            flag = 1
            for ch in word:
                idx = s.find(ch,i)
                if idx == -1:
                    flag = 0
                    break
                i = idx+1
            if flag : res += 1
        return res