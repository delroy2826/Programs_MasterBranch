mode  = 'e'
str1 = "Hello World"
key = 1
translated = ""
for i in str1:
    if mode == "e":
        translated += chr(ord(i)+int(key))
    else:
        translated+=chr(ord(i)-int(key))
print(translated)
newstr=""
for i in translated:
    newstr+=chr(ord(i)-int(key))
print(newstr)