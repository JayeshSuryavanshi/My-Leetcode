class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = collections.Counter(ransomNote)
        b = collections.Counter(magazine)
        return not collections.Counter(ransomNote) - collections.Counter(magazine)