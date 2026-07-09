class Solution:
    def isPalindrome(self, x: int) -> bool:
        output = False
        reversed = 0
        if x >= 0:
            temp = x
            while temp > 0:
            # To reverse the digits we continuously take the last digit of the number
            # and append it to the reversed variable
                reversed = temp % 10 + reversed * 10
                temp = temp // 10

            if reversed == x:
                output = True
        return output




s = Solution()
print(s.isPalindrome(0))