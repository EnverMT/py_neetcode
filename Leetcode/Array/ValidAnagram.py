class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        storeS = dict()
        storeT = dict()
        for i in range(len(s)):
            storeS[s[i]] = storeS.get(s[i], 0) + 1
            storeT[t[i]] = storeT.get(t[i], 0) + 1

        return storeS == storeT
