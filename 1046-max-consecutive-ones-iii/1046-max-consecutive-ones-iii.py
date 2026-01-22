class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        seen = 0
        window_start = 0
        if 0 not in arr:
            return len(arr)

        for window_end in range(len(arr)):
            char = arr[window_end]

            if char == 0:
                seen += 1
            
            if seen > k:
                window_start_char = arr[window_start]
                if window_start_char == 0:
                    seen -= 1
                window_start += 1
            
        return window_end - window_start + 1
        # count = {0:0, 1:0}
        # window_start = 0
        # max_length = 0

        # if 0 not in arr:
        #     return len(arr)

        # for window_end in range(len(arr)):

        #     char = arr[window_end]
        #     count[char] += 1

        #     while count[0] > k:
        #         window_start_char = arr[window_start]
        #         count[window_start_char] -= 1

        #         window_start += 1
                
        #     current_length = window_end - window_start + 1
        #     max_length = max(current_length, max_length)
        # return max_length