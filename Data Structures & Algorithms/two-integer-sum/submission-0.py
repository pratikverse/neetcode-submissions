class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for index, value in enumerate(nums):
            complement = target - nums[index]
            if complement in my_map:
                return [my_map[complement],index]
            else:
                my_map[value] = index 
            