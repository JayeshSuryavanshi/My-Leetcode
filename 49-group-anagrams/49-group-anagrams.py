class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for st in strs:
            s = ''.join(sorted(st))
            dictionary[s].append(st)
        return sorted(dictionary.values())