class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for left in range(len(numbers)-1):
            right = len(numbers)-1
            while left < right:
                required_sum = numbers[left] + numbers[right]
                if required_sum == target:
                    return [left+1, right+1]
                elif required_sum < target:
                    left += 1
                elif required_sum > target:
                    right -= 1
                
                
        
                