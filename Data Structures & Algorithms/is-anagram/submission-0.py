class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dictt = {}

        if len(s) != len(t):
            return False

        for a in s:
            if a not in dics:
                dics[a] = 1
            else:
                dics[a] += 1

        for b in t:
            if b not in dictt:
                dictt[b] = 1
            else:
                dictt[b] += 1

        return dics == dictt

        