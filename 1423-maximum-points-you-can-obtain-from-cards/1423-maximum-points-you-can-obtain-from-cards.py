class Solution:
    def maxScore(self, C: List[int], K: int) -> int:
        score = sum(C[:K])
        total = sum(C[:K])
        for i in range (K-1, -1, -1):
            total = total + C[i + len(C) - K] - C[i]
            score = max(score, total)
        return score
                
        