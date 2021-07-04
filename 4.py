mode = input("Select the Option.\n1.Encryption\n2.Descryption\n")
message = input("Enter the message to be Encrypted or Decrypted:\n")
key = input("Enter the Secret Key number:\n")
conmessage = ""
for i in message:
    if mode=="1":
        conmessage+=chr(ord(i)+int(key))
    else:
        conmessage+=chr(ord(i)-int(key))

print(conmessage)


#Fgntq{"Qnkxgktc