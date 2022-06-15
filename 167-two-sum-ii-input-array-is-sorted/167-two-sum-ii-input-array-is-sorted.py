class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        dictionary = {}
        
        for i in range(len(numbers)):
            if target-numbers[i] in dictionary:
                return [dictionary[target-numbers[i]] + 1, i + 1] # dictionary lookup
            else:
                dictionary[numbers[i]] = i #filling dictionary
                
                
#         i = 0
#         j = len(numbers)-1
        
#         while i < j:
#             potentialMatch = numbers[i] + numbers[j]
#             if potentialMatch == target:
#                 return [i + 1, j + 1]
#             elif potentialMatch < target:
#                 i = i + 1
#             else:
#                 j = j - 1
                
