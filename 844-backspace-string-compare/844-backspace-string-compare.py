class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S = []
        T = []
        for i in s:
            if i == '#':
                if S != []:
                    S.pop()
            else:
                S.append(i)
        for i in t:
            if i == '#':
                if T != []:
                    T.pop()
            else:
                T.append(i)
        return S == T


        