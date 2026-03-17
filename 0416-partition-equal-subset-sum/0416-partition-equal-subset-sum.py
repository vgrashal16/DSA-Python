class Solution:
    def f(self, index, nums, target, dp):
        if target == 0: return True
        if index == 0: return nums[0]==target

        if (dp[index][target] != -1):
            return dp[index][target] == 1

        not_take = self.f(index-1, nums, target, dp)

        take = False

        if nums[index] <= target:
            take = self.f(index-1, nums, target-nums[index], dp)
        
        ans = not_take or take

        dp[index][target] = ans

        return ans

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        for x in nums:
            total_sum += x
        
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum//2
        dp = [[-1] * (target_sum+1) for _ in range(len(nums))]

        return self.f(len(nums)-1, nums, target_sum, dp)