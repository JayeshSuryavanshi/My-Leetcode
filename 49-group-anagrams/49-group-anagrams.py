class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for word in strs:
            dictionary[''.join(sorted(word))].append(word)
        return dictionary.values()