class Solution:
    def findComplement(self, num: int) -> int:
        power_of_two = 1
        while power_of_two <= num:
            power_of_two <<= 1
        
        return num ^ (power_of_two - 1)