class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        half = len(arr) // 2
        sorted_order = sorted(c.values(), reverse = True)
        print(sorted_order)
        
        sums = 0
        count = 0
        for i in range(len(sorted_order)):
            sums += sorted_order[i]
            count += 1
            if (sums >= half):
                return count
        