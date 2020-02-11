class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Since every elements appear twice except for one.
        # XOR all elements in nums will result the single element
        ans = 0
        for n in nums:
            ans ^= n
        
        return ans