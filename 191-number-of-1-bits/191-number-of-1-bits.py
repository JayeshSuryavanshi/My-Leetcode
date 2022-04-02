class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #convert to binary
        binary = bin(n)
        
        #initialize counter object
        count = Counter(binary)
        
        return count['1']