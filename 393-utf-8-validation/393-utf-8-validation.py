class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def res(i):
            if len(data) < i: return False
            for _ in range(i):
                if not data.pop().startswith("10"): return False
            return True
        
        data = [str(bin(seq)[2:].zfill(8)) for seq in data[::-1]]
        while data:
            sequence = data.pop()
            if sequence.startswith("0"): continue
            if sequence.startswith("110"):
                if not res(1): return False
            elif sequence.startswith("1110"):
                if not res(2): return False
            elif sequence.startswith("11110"):
                if not res(3): return False
            else: return False
        return True