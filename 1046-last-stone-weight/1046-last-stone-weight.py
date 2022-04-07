from sortedcontainers import SortedList
# external library which is faster than standard python libraries
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_list = SortedList(stones)
        while len(sorted_list) >= 2:
            a = sorted_list.pop()
            b = sorted_list.pop()
            if a > b: 
                sorted_list.add(a - b)
        if len(sorted_list):
            return sorted_list.pop()
        else:
            return 0