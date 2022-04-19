from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a, b= Counter(ransomNote), Counter(magazine)
        return not collections.Counter(ransomNote) - collections.Counter(magazine)