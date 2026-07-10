class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        # I will save the roman numbers in a dictionary
        roman_nums_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(s)):
            value = roman_nums_dict[s[i]]
            # if next symbol is larger, this is subtractive
            if i + 1 < len(s) and roman_nums_dict[s[i+1]] > value:
                total -= value
            else:
                total += value
        return total





s = Solution()
print(s.romanToInt("III"))