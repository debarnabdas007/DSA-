class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False # negative numbers are never palindrom

        original = x
        reverse_num = 0
        while x > 0:
            digit = x % 10
            reverse_num = reverse_num*10 + digit
            x = x // 10

        if reverse_num == original:
            return True
        else:
            return False    