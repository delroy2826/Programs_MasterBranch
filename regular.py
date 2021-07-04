import re       #(\w\w\:){5}\w+ -mac address
text_to_search = '''
\t_abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Delroy Allen
Delroy Chuck

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

cat
bat
mat
asda\asdc\qwrec\asdc
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T Delroy

@gmail.Com
CoreyMSchafer@gmail.Com
corey.schafer@university.edu
corey-321-schafer@my-work.net
murty@gmail.com  00:0a:95:9d:68:16
53:F2:47:2D:BB:1E
26:EA:6C:4C:B7:6B
08:81:3F:CC:08:FD
A6:85:06:B7:97:38
06:A7:44:FD:8B:24
42:C3:CC:CB:8A:45
'''
mac = "00:0a:95:9d:68:16"
sentence = "Start a sentence and then bring it to an end sentence"
pattern=re.compile(r'(\w\w:){5}\w\w')
match = pattern.finditer(text_to_search)
for i in match:
    print(i)