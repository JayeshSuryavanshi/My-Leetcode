class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums1 = [] * len(nums)
        # for i in nums:
        #     nums1.append(i)
        # for i in nums:
        #     nums1.append(i)
        # return nums1
        nums.extend(nums)
        return nums