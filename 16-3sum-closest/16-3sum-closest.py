class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        res = sum(nums[:3])
        for i in range(0,len(nums)):
            j = i+1
            k = len(nums)-1 
            while(j < k):
                s = sum((nums[i], nums[j], nums[k]))
                if(abs(s-target) < abs(res-target)):
                    res = s
                if(s < target):
                    j += 1
                elif(s > target):
                    k -= 1
                else:
                    return res
        return res