class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        final = []
        size = 0
        for (w, h) in envelopes:
            if not final or h > final[-1]:
                final.append(h)
                size += 1
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if final[m] < h:
                        l = m + 1
                    else:
                        r = m
                final[l] = h
        return size