class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # Initialize the variables
        max_sum,curr_sum = nums[0],0

        # Iterate through the array
        for num in nums:
            if curr_sum <0:
                curr_sum = 0
            curr_sum+=num
            max_sum = max(max_sum,curr_sum)
        return max_sum
        