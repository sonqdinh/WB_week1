class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True
        
        count = [0, 0]
        for bill in bills:
            if bill == 5:
                count[0] += 1
            elif bill == 10:
                if not count[0]:
                    return False
                count[0] -= 1
                count[1] += 1
            elif bill == 20:
                if (count[1] and not count[0]) or (not count[1] and count[0] < 3):
                    return False
                
                if count[1]:
                    count[1] -= 1
                    count[0] -= 1
                else:
                    count[0] -= 3
        
        return True