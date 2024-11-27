from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1)> len(nums2)):
            nums1,nums2 = nums2,nums1
        mapp={}
        res=[]
        for num in nums1:
            mapp[num] = mapp.get(num,0)+1
        for num in nums2:
            if mapp.get(num,0)>0:
                res.append(num)
                mapp[num]-=1
        return res    