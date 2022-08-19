class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def combs(a):
            if len(a) == 0:
                return [[]]
            cs = []
            for c in combs(a[1:]):
                cs += [c, c+[a[0]]]
            return cs
        
        return combs(nums)