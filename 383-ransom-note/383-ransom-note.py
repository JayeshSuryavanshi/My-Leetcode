from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        result = (collections.Counter(ransomNote) - collections.Counter(magazine))
        return not result