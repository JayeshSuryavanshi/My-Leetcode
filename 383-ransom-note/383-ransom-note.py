class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)
        return not ransom - mag
        