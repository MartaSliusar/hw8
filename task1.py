def roman_to_integer(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    while True:
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                integer += roman[s[i]]-roman[s[i-1]]
            else:
                integer += roman[s[i]]
        return integer

s = "LVIII"
print(roman_to_integer(s))
