#Given an input string Count all lower case, upper case, digits, and special symbols
#findDigitsCharsSymbols("P@#yn26at^&i5ve") = Chars = 8 Digits = 3 Symbol = 4
#Given an input string Count all lower case, upper case, digits, and special symbols
#findDigitsCharsSymbols("P@#yn26at^&i5ve") = Lower Case 7, Upper Case 1, Digits 3, Special Symbols 4
def count(str1):
    lowercase_chars = 0
    uppercase_chars = 0
    digits = 0
    special_symbols= 0
    for i in str1:
        if i.islower():
            lowercase_chars+=1
        elif i.isupper():
            uppercase_chars+=1
        elif i.isdigit():
            digits+=1
        else:
            special_symbols+=1
    return "Lower Case {}, Upper Case {}, Digits {}, Special Symbols {}".format(lowercase_chars,uppercase_chars,digits,special_symbols)

str1 = 'P@#yn26at^&i5ve'
print(count(str1))