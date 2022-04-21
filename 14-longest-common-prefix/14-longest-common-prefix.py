class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        _zip = list(zip(*S))
        common_prefix = ""
        for i in _zip:
            if len(set(i)) == 1:
                common_prefix += i[0]
            else:
                break
        return common_prefix
                