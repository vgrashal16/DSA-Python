class Solution:
    def minSwaps(self, arr: List[int]) -> int:
        n = len(arr)
        count = sum(arr)
        
        if count == 0 or count == n:
            return 0
        bad = 0
        for i in range(count):
            if arr[i] == 0: 
                bad += 1

        min_bad = bad
        window_start = 0

        for window_end in range(count, n + count - 1):
            if arr[window_end % n]==0:
                bad += 1
            if arr[window_start % n]==0:
                bad -= 1
            
            window_start += 1
            min_bad = min(min_bad, bad)

        return (min_bad)