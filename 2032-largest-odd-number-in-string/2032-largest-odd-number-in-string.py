class Solution:
    def largestOddNumber(self, string: str) -> str:
        result = ""
        last_odd_index = -1
        for x in range(len(string)-1, -1, -1):
            if int(string[x]) % 2 != 0:
                last_odd_index = x
                break
        
        result = string[:last_odd_index+1]
        return (result)