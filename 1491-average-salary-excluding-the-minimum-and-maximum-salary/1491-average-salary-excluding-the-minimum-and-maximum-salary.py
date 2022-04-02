class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = max(salary)
        minimum = min(salary)
        j = 0
        
        for i in salary:
            j = j + i
        return ((j - maximum - minimum)/(len(salary)-2))
            
            
            