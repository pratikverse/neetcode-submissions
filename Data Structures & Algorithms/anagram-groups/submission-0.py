class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for word in strs:

            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] +=1

            key = tuple(count)

            if key not in mpp:
                mpp[key] = []
            
            mpp[key].append(word)
        
        result = list(mpp.values())
        return result




