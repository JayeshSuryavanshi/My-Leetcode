class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        for i, c in enumerate(candidates):
            if c > target:
                continue
            elif c == target:
                ret += [[c]]
            else:
                ret += [[c] + x for x in self.combinationSum(candidates[i:], target-c)]
        return ret