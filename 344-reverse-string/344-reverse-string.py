class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Two Pointer Approach - Optimal
        i = 0
        j = len(s)-1
        
        while i <= j:
            # swap in-place
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s