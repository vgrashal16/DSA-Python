class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False

        target = total//k
        seen = [False] * len(nums)

        nums.sort(reverse = True)
        def backtrack(index, k_left, subsetSum):
            if k_left == 1: return True

            if subsetSum == target:
                return backtrack(0, k_left-1, 0)
            
            for i in range(index, len(nums)):

                if subsetSum + nums[i] > target: continue
                
                if seen[i] == True: continue

                seen[i] = True

                if backtrack(i + 1, k_left, subsetSum + nums[i]): return True

                seen[i] = False

                while i + 1 < len(nums) and nums[i + 1] == nums[i]: i+=1
                if subsetSum == 0: return False
            return False
        
        return backtrack(0, k, 0)
