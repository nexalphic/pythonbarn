import string
def ccipher(encode, key):
    crypted = ""
    for ch in encode:
        crypted = crypted + string.ascii_lowercase[encode.find(ch) + key]
    print crypted
ccipher("hello", 2)
