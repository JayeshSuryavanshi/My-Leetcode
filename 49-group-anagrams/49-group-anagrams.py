class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            
            if sorted_string not in dictionary:
                dictionary[sorted_string] = []
            dictionary[sorted_string].append(string)
            
        return list(dictionary.values())