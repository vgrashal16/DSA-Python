class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        result = ""
        
        min_length = 0
        max_length = 0
        left_over = ""
        
        if len(s1) > len(s2):
            min_length = len(s2)
            max_length = len(s1)
            left_over = s1
        elif len(s2) > len(s1):
            min_length = len(s1)
            max_length = len(s2)
            left_over = s2
        else:
            min_length = max_length = len(s1)

        for i in range(min_length):
            result += s1[i]
            result += s2[i]
        

        for i in range(min_length, max_length):
            result += left_over[i]
        
        return(result)
