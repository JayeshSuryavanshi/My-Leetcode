from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        return not collections.Counter(ransomNote) - collections.Counter(magazine)