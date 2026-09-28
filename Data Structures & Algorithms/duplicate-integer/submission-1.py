class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        # using dict

        uniques = {}
        for num in nums:
            if num not in uniques:
                uniques[num] = 0
            uniques[num] += 1

        
        for key, val in uniques.items():
            if val > 1:
                return True
        return False