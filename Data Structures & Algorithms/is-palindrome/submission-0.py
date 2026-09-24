class Solution:
    def isPalindrome(self, s):
        start = 0
        finish = len(s) - 1
        
        while start < finish:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[finish].isalnum():
                finish -= 1
                continue
            if s[start].lower() == s[finish].lower():
                start += 1
                finish -= 1
            else:
                return False

        return True