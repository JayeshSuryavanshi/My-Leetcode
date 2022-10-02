class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # collections - defaultdict
        dictionary = collections.defaultdict(list)
        # traverse every string in strings
        for st in strs:
            s = ''.join(sorted(st))
            # in defaultdict we can append just like list
            dictionary[s].append(st)
            # returning the dictionary values in 
        return sorted(dictionary.values())