class Solution:

    def isHappy(self, n: int) -> bool:

        hashtable = {}

        while True:

            a = 0

            while n > 0:
                digit = n % 10
                n = n // 10
                a += digit ** 2

            if a in hashtable:
                return False

            if a == 1:
                return True

            hashtable[a] = True
            n = a  