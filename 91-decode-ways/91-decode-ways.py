class Solution:
	def numDecodings(self, s: str) -> int:
		if s[0] == '0': return 0

		prev_1, prev_2 = 1, 1

		for i in range(1, len(s)):            
			curr = 0
			if s[i] != '0':
				curr += prev_2

			if 10 <= int(s[i-1:i+1]) <= 26:
				if i > 1:
					curr += prev_1
				else:
					curr +=1

			prev_1 = prev_2
			prev_2 = curr

		return prev_2