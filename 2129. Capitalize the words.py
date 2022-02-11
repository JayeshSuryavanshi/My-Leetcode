class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        final = []
        
        for word in title.split():
            
            if len(word) < 3:
                final.append(word.lower())
                
            elif word != word.istitle():
                final.append(word.capitalize())
                
        return ' '.join(final)  