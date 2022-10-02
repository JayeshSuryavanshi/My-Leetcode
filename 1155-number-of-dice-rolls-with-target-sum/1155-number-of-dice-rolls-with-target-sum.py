class Solution:
    def rec(self, n, k, target, lookup):
        if target <= 0 or target > n*k:
            return 0
        if n == 1 and target <= k:
            return 1
        if (n, target) not in lookup:
            ways = 0
            for val in range(1, k+1):
                ways += (self.rec(n-1, k, target-val, lookup))
            lookup[(n, target)] = ways
        return lookup[(n, target)] 
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.rec(n, k, target, {}) % ((10**9) + 7)