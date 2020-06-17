class Solution:

    def run(self, n):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        n_in_roman_alphabet = ''
        i = 0
        while n > 0:
            for _ in range(n // val[i]):
                n_in_roman_alphabet += syb[i]
                n -= val[i]
            i += 1
        return n_in_roman_alphabet


print(Solution().run(1054))
