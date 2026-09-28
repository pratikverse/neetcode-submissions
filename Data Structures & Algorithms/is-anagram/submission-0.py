class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mppS = {}
        mppT = {}

        for ch in s:
            mppS[ch] = mppS.get(ch,0)+1
        for ch in t:
            mppT[ch] = mppT.get(ch,0)+1
        return mppS == mppT
        