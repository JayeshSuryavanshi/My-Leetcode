class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
            if not nums:
                return 0

            length = 1
            flag = None # current is increasing or not
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1] and flag != True:
                    length += 1
                    flag = True
                if nums[i] < nums[i - 1] and flag != False:
                    length += 1
                    flag = False
            return length
        
        