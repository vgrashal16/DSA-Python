class Solution:
    def trap(self, nums: List[int]) -> int:
        def prefix_max(nums):
            left_max = [0] * len(nums)
            left_max[0] = nums[0]

            for i in range (1, len(nums)):
                left_max[i] = max(left_max[i-1], nums[i])
            
            return left_max

        def suffix_max(nums):
            right_max = [0] * len(nums)
            right_max[len(nums)-1] = nums[len(nums)-1]

            for i in range (len(nums)-2, -1, -1):
                right_max[i] = max(right_max[i+1], nums[i])
            
            return right_max

        n = len(nums)
        i = 0
        area = 0
        left_max = prefix_max(nums)
        right_max = suffix_max(nums)

        for i in range(0, n):
            area += min(left_max[i], right_max[i]) - nums[i]
        
        return (area)
                
