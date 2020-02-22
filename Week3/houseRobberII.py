class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(first = True):
            value = [[0]*(len(nums) - 1) for _ in range(2)]
            
            value[1][0] = nums[0] if first else nums[1]
            
            if first:
                for i in range(1, len(nums) - 1):
                    value[0][i] = max(value[0][i - 1], value[1][i - 1])
                    value[1][i] = nums[i] + value[0][i - 1]
            else:
                for i in range(2, len(nums)):
                    value[0][i - 1] = max(value[0][i - 2], value[1][i - 2])
                    value[1][i - 1] = nums[i] + value[0][i - 2]
            
            return max(value[0][-1], value[1][-1])
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(solve(False), solve())