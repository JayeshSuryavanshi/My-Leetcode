class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [combs for combs in combinations(range(1, 10), k) if sum(combs) == n]
        