class Solution:
    def searchMatrix(self, matrix, target):
        j = len(matrix[0]) - 1
        
        for row in matrix:
            while j >= 0 and row[j] > target: j -= 1
            if j < 0: break
            if row[j] == target: 
                return True
        return False