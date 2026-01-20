class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        window_start = 0
        seen = set()  # The "Bouncer" tracking who is in the window

        for window_end in range(len(nums)):
            # --- PHASE 1: Handle Conflicts (The "While" Loop) ---
            # Before we let the new guy (arr[window_end]) in, we check the set.
            # If he is already in there, we kick people out from the LEFT
            # until the duplicate is gone.
            while nums[window_end] in seen:
                current_sum -= nums[window_start]
                seen.remove(nums[window_start])
                window_start += 1

            # --- PHASE 2: Add New Element ---
            # Now it's safe to add the new element
            seen.add(nums[window_end])
            current_sum += nums[window_end]

            # --- PHASE 3: Check Size & Update Max ---
            # We only care if the window size is EXACTLY k
            if (window_end - window_start + 1) == k:
                max_sum = max(max_sum, current_sum)

                # --- PHASE 4: Slide the Window ---
                # To move to the next iteration, we must maintain the size k.
                # So we remove the left-most element to make room for the next step.
                current_sum -= nums[window_start]
                seen.remove(nums[window_start])
                window_start += 1

        return max_sum