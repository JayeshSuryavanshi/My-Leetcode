class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Naive Approach - Square Root - TC: O(sqrt(n))
        
        # for i in range(1, num + 1):
        #     if i * i == num:
        #         return True
        #     elif i * i > num:
        #         return False
        
        # Binary Search Approach - TC: O(log(n))
        
        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            if mid * mid > num:
                right = mid - 1         
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        return False