class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            max_length = 0
            window_start = 0
            max_repeat_count = 0
            
            for window_end in range(len(s)):
                right_char = s[window_end]

                count[right_char] = count.get(right_char, 0) + 1
                
                max_repeat_count = max(max_repeat_count, count[right_char])

                current_length = window_end - window_start + 1
                
                if current_length - max_repeat_count > k:
                    left_char = s[window_start]
                    count[left_char] -= 1
                    window_start += 1
                    
                max_length = max(max_length, window_end - window_start + 1)
                
            return max_length