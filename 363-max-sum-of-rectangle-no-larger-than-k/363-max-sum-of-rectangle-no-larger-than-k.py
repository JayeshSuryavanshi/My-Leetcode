class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)] 
        for row in range(rows):
            sum_left = 0
            for col in range(cols):
                sum_above = prefix_sum[row - 1][col]
                sum_left += matrix[row][col]
                prefix_sum[row][col] = sum_above + sum_left
                
        max_sum_lk = float('-inf')
        for row1 in range(rows):
            for row2 in range(row1, rows):
                left_sums = [0]

                for end_col in range(cols):
                    sum_here = prefix_sum[row2][end_col] - prefix_sum[row1 - 1][end_col]
                    
                    ins = bisect_right(left_sums, sum_here - k)
                    if ins > 0 and left_sums[ins - 1] == sum_here - k:
                        return k
                    elif ins <= end_col:
                        max_sum_lk = max(max_sum_lk, sum_here - left_sums[ins])
                        
                    insort(left_sums, sum_here)

        return max_sum_lk