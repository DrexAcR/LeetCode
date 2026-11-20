class Solution:
    def intToRoman(self, num: int) -> str:
        roman_nums_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        roman = ""
        while num > 0:
            for roman_num, value in sorted(roman_nums_dict.items(), key=lambda x: x[1], reverse=True):
                if num >= value:
                    num -= value
                    roman += roman_num
                    break
        return roman

s = Solution()
print(s.intToRoman(67))  
    




         
