class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        final = []
        
        for i in range(len(accounts)):
            final.append(sum(accounts[i]))
            
        return max(final)
        