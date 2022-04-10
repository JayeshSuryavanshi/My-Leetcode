class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        scoreboard = []
        
        for op in ops:
            if op == 'C':
                scoreboard.pop()
                
            elif op == 'D':
                scoreboard.append(2 * scoreboard[-1])
                
            elif op == '+':
                scoreboard.append(scoreboard[-1] + scoreboard[-2])
                
            else:
                scoreboard.append(int(op))
                
        return sum(scoreboard)
            