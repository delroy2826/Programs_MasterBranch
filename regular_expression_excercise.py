#1 Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
def check(str1):
    match = pattern.search(str1)
    return not bool(match)

pattern = re.compile(r'[^\w+]')
str1 = "delro3y1229"
print(check(str1))
str1 = "delro#3y1229"
print(check(str1))
#Solution from web
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))

#2 Write a Python program that matches a string that has an (a ) followed by (zero or more b's)
import re
str1 = "abbc"
pattern = re.compile(r'ab*')
match = pattern.finditer(str1)
for i in match:
    print(i)

import re
def check(str1):
    pattern=r'ab*'
    if re.search(pattern,str1):
        print("Found Match")
    else:
        print("Not Found Match")
check("ab")
check("cb")
check("abbbbb")
check("abbwww")

#3  Write a Python program that matches a string that has an (a) followed by (one or more b's)
import re
str1 = "abcs"
pattern = re.compile(r'ab+')
match = pattern.finditer(str1)
for i in match:
    print(i)

import re
def check(str1):
    pattern = r'ab+'
    if re.search(pattern,str1):
        print("Found Match")
    else:
        print("Not Found")
check("ab")
check("cb")
check("abbbbb")
check("a")

#4 Write a Python program that matches a string that has an a followed by zero or one 'b'
import re
def check(str1):
    pattern = re.compile(r'ab?')
    if re.search(pattern,str1):
        print("Match")
    else:
        print("No Match")
l = ['ab','abc','abbc','aabbc','qwe']
for i in l:
    check(i)

#5 Write a Python program that matches a string that has an a followed by three 'b'

import re
def check(str1):
    pattern = re.compile(r'ab{3,}')
    if re.search(pattern,str1):
        print("Match")
    else:
        print("No Match")
l = ['ab','abbb','aabbbbbc','aabbbc','qwe']
for i in l:
    check(i)

#6 Write a Python program that matches a string that has an a followed by two to three 'b'
import re
def check(str1):
    pattern = re.compile(r'ab{2,3}?')
    if re.search(pattern,str1):
        print("Match")
    else:
        print("No Match")
l = ['ab','abbb','aabbbbbc','aabbbc','qwe']
for i in l:
    check(i)

#7 Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
def check(str1):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    if re.search(pattern,str1):
        print("Match")
    else:
        print("No Match")
l = ['aab_cbbbc','aab_Abbbc','Aaab_abbbc']
for i in l:
    check(i)
