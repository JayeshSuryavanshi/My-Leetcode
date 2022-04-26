class Solution:
    def reverseBits(self, n: int) -> int:   
        #  formatting 'n' in 32 bit binary
        bits = '{0:032b}'.format(n)
        # reversing the bits
        reverse_bits = bits[::-1]
        # finally we have to return as int
        return int(reverse_bits, 2)

