from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            if (self.evenDigits(num)):
                ans+=1
        return ans
    def evenDigits(self,num:int)->bool:
        digitcount=0
        while (num!=0):
            digitcount+=1
            num//=10
        return digitcount%2==0