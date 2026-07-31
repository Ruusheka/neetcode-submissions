class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue

            l=i+1
            r=n-1
            while l<r:
                sumT=a+nums[l]+nums[r]
                if sumT>0:
                    r-=1
                elif sumT<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        
        return ans
        