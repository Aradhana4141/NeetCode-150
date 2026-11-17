#using backtracking pattern
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def bck(start,path):
            if sum(path)==target:
                ans.append(path.copy())
                return
            if sum(path)>target:
                return 
            
            for i in range(start, n):
                path.append(nums[i])
                bck(i,path) # y not i+1 bcz duplicates are allowed
                path.pop()
        bck(0,[])
        return ans
