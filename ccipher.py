letters = "abcdefghijklmnopqrstuvwxyz"
def ccipher(encode, key):
    crypted = ""
    for ch in encode:
        crypted = crypted + chr(ord(ch) + key)
    print crypted
    
#Example input:
ccipher("hello", 1)
