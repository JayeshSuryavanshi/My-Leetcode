class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        _zip = list(zip(*S))
        prefix = ""
        for i in _zip:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
                