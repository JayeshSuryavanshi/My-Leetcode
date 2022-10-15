class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def compressed_length(seqlen):
            if not seqlen: return 0
            if seqlen == 1: return 1
            if seqlen < 10: return 2
            if seqlen < 100: return 3
            if seqlen < 1000: return 4

        @lru_cache(None)
        def min_length(from_idx=0, last_char='', last_count=0, remains=k):
            if from_idx >= len(s): return compressed_length(last_count)

            possible_lengths = []

            if remains:
                possible_lengths += [min_length(from_idx+1, last_char, last_count, remains-1)]
            if s[from_idx] == last_char: 
                possible_lengths += [min_length(from_idx+1, last_char, last_count+1, remains)]
            else: 
                possible_lengths += [min_length(from_idx+1, s[from_idx], 1, remains) + compressed_length(last_count)]

            return min(possible_lengths)

        return min_length()