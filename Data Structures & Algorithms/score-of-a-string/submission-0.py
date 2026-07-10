class Solution:
    def scoreOfString(self, s: str) -> int:
        summa = 0
        index = 0
        while (index != len(s)-1):
            summa += abs((ord(s[index]))-ord(s[index +1]))
            index += 1
        return summa


        
        