class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = [1]
        e = [1]
        i = [1]
        o = [1]
        u = [1]
        
        for _ in range(n-1):
            a.append(e[-1])
            e.append(a[-2] + i[-1]) 
            i.append(a[-2] + e[-2] + o[-1] + u[-1])
            o.append(i[-2] + u[-1])
            u.append(a[-2])

        return (a[-1] + e[-1] + i[-1] + o[-1] + u[-1]) % (10**9+7)
		