class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = []
        n = len(nums)

        for num in nums:
            output.append(prefix)
            prefix *=num

        for i in range(n-1,-1, -1 ):
            output[i] *= postfix
            postfix *=nums[i]
        return output
        
            



       
        
        
        

