import string
str1 = input("")
str2 = ""
count_consonants = 0
count_special=0
count_vowel = 0
for i in str1.lower():
    if i in "aeiou":
        count_vowel +=1
    if i not in "aeiou " + string.punctuation:
        count_consonants +=1
    if i in string.punctuation + " ":
        count_special += 1
for i in str1:
    if i in string.punctuation:
        continue
    if i.isupper():
        str2 +=i.lower()
    else:
        str2 +=i.upper()
print("Vowels in a string:",count_vowel)
print("Consonants in a string:",count_consonants)
print("Special Characters in a string:",count_special)
print("{} to {}".format(str1,str2))