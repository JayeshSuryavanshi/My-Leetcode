class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums = set(numbers)
        # nums1 = list(nums)
        print(numbers)
        i = 0
        j = len(numbers)-1
        
        while i < j:
            potentialMatch = numbers[i] + numbers[j]
            if potentialMatch == target:
                return [i + 1, j + 1]
            elif potentialMatch < target:
                i = i + 1
            else:
                j = j - 1
                
