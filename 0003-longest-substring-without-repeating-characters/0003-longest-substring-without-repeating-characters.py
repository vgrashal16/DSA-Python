class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        window_start = 0
        hashmap = {}

        for window_end in range(len(s)):
            char = s[window_end]
            
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1

            length = max(length, len(hashmap))

            while len(hashmap) != sum(hashmap.values()):
                window_start_char = s[window_start]
                hashmap[window_start_char] -= 1
                if hashmap[window_start_char] == 0:
                    del hashmap[window_start_char]
                window_start += 1

        return length