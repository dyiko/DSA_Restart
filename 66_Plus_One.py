from typing import List
def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        res=[0]*len(digits)

        for i in range(len(digits)-1,-1,-1):
            total=digits[i]+carry
            res[i]=total%10
            carry=total//10
        if carry>0:
            return [carry]+res 
        return res