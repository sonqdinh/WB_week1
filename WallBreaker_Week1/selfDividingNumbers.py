class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def checkDivisible(n):
            if n == 0:
                return False
            
            nValue = n
            while n:
                div = n % 10
                if div == 0:
                    return False
                elif nValue % div:
                    return False
                
                n //= 10
            
            return True
        
        ans = []
        for n in range(left, right + 1):
            if checkDivisible(n):
                ans.append(n)
        
        return ans