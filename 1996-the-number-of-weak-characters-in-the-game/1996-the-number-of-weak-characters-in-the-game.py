class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0],x[1]))
        result = 0
        maximum = 0
        print(properties)
        for attack, defence in properties:
            if (defence < maximum):
                result += 1
            else:
                maximum = defence
        return result
