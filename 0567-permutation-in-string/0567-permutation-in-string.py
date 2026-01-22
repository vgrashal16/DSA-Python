class Solution:
    def checkInclusion(self, perm: str, s: str) -> bool:
        if len(perm) > len(s): 
            return False
    
        perm_hash = {}
        for x in perm:
            perm_hash[x] = perm_hash.get(x, 0) + 1
        
        seen = {}
        window_start = 0

        for window_end in range(len(s)):
            right_char = s[window_end]
            seen[right_char] = seen.get(right_char, 0) + 1

            current_length = window_end - window_start + 1
            if current_length > len(perm):
                left_char = s[window_start]
                seen[left_char] -= 1

                if seen[left_char] == 0:
                        del seen[left_char] 

                window_start += 1

            if seen == perm_hash:
                return True
        return False