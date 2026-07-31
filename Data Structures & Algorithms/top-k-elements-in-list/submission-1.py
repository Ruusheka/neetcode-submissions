class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans={}

        for i in nums:
            ans[i]= 1+ans.get(i,0)
        
        ans=sorted(ans,key=ans.get,reverse=True)
        
        return ans[:k]

            