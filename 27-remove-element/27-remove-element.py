class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        while k < len(nums):
            if nums[k] == val:
                del nums[k]
            else:
                k += 1
                