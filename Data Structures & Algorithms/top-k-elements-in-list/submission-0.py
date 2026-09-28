class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = defaultdict(int)

        for num in nums:
            mpp[num]+=1
        
        sorted_mpp = dict(sorted(mpp.items(), key=lambda x: x[1], reverse=True))

        keys = list(sorted_mpp.keys())[:k]
        return keys