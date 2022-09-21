class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(x for x in nums if x % 2 == 0)
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0: evenSum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0: evenSum += nums[idx]
            ans.append(evenSum)
        return ans