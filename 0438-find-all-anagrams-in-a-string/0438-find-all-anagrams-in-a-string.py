class Solution:
    def findAnagrams(self, s: str, perm: str) -> List[int]:
        if len(perm) > len(s):
            return []
    
        perm_hash = {}
        for char in perm:
            perm_hash[char] = perm_hash.get(char, 0) + 1

        window_start = 0
        seen = {}
        result = []

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
                result.append(window_start)
        
        return result