class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1

        res = []
        for k, v in sorted(cnt.items(), key = lambda x: -x[1]):
            res += [k] * v
        return "".join(res)