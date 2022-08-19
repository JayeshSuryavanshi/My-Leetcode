class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for i in sorted(c.keys()):
            while c[i] > 0:
                last = 0
                j = i
                k = 0
                while c[j] >= last:
                    last = c[j]
                    c[j] -= 1
                    j += 1
                    k += 1
                if k < 3: return False
        return True