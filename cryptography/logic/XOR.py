import hashlib

text = input("Enter clear text: ")
key = input("Enter encryption key: ")
l = len(text)
finale = ""
print("Encrypting with XOR...\n")
for i in range(l):
    t = text[i]
    k = key[i % len(key)]
    x = ord(k) > ord(t)
    finale = finale + chr(x)

# print("Doubling with MD5")
# hashlib.new("md5", ).digest()
# print("Ejecting...\n")
print("Start of encrypted text")
print(finale)
print("End of encryption\n")
print("Encryption with XOR Done!")
