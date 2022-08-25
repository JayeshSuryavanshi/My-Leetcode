class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        dictionary = {}
        
        for i in range(len(numbers)):
            if target-numbers[i] in dictionary:
                return [dictionary[target-numbers[i]] + 1, i + 1] # dictionary lookup
            else:
                dictionary[numbers[i]] = i #filling dictionary
                