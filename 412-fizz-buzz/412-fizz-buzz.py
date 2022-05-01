class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        output_list = []
        
        for i in range(1, n + 1):
            
            if i % 3 == 0 and i % 5 == 0:
                output_list.append('FizzBuzz')
            
            elif i % 3 == 0:
                output_list.append('Fizz')
            
            elif i % 5 == 0:
                output_list.append('Buzz')
            
            else:
                output_list.append( str(i) )
                
        return output_list