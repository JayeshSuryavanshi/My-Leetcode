class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {    '2':'abc',
                       '3':'def', 
                       '4':'ghi',
                       '5':'jkl',
                       '6':'mno',
                       '7':'pqrs',
                       '8':'tuv',
                       '9':'wxyz'
                  }

        #recursive approach
        def recursive(i=0, combo="", out=[]):
            if i == len(digits):
                out.append(combo)
            else:
                nextDigit = digits[i]
                children = mapping[nextDigit]
                for child in children:
                    recursive(i+1, combo+child, out)
            
            return out        
        return recursive(0, "", [])