class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        max_profit = 0
        mini = arr[0]
        n = len(arr)
        for i in range(1, n):
            max_profit = max(max_profit, arr[i]-mini)
            mini = min(mini, arr[i])
        
        return max_profit
