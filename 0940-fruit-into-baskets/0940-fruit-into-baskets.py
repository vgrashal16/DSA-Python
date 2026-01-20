class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        max_len = 0
        window_start = 0
        hashmap = {}

        for window_end in range(len(arr)):
            char = arr[window_end]
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1

            while len(hashmap) > 2:
                window_start_char = arr[window_start]
                hashmap[window_start_char] -= 1

                if hashmap[window_start_char] == 0:
                    del hashmap[window_start_char]
                
                window_start += 1
            
            max_len = max(max_len, sum(hashmap.values()))
        
        return max_len