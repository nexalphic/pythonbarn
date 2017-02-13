letters = "abcdefghijklmnopqrstuvwxyz"
def ccipher(encode, key):
    result = ""
    mode = int(input("Would you like to (1)encrypt or (2)decrypt?"))
    if mode == 1:
        for ch in encode:
            result = result + chr(ord(ch) + key)
    elif mode == 2:
        for ch in encode:
            crypted = crypted + chr(ord(ch) - key)
    else:
        print "mode number not recognized"
    print result
    
#Example input:
print ccipher(input"Input string.")
