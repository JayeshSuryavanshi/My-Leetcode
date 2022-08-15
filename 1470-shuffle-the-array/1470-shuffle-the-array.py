class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []     
        for number in range(n):
            shuffled.append(nums[number])
            shuffled.append(nums[n + number])
        return shuffled
        