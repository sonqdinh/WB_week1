class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in reversed(range(len(digits))):
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            if not carry:
                return digits
            
        if carry:
            digits.append(1)
            digits[0], digits[-1] = digits[-1], digits[0]
        
        return digits
            