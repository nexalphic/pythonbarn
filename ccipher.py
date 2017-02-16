letters = "abcdefghijklmnopqrstuvwxyz"
def ccipher():
    result = ""
    encode = str(input("Input a string."))
    mode = input("Would you like to encrypt, decrypt, or brute force?")
    if mode in [1, "encrypt", "e", "Encrypt", "E"]:
        key = int(input("Input a key."))
        for ch in encode:
            result = result + chr(ord(ch) + key)
    elif mode in [2, "decrypt", "e", "Decrypt", "E"]:
        key = int(input("Input a key."))
        for ch in encode:
            result = result + chr(ord(ch) - key)
    elif mode in [3, "brute force", "b", "brute", "force"]:
        times = int(input("How many times would you like to brute force?"))
        key = 1
        for times in range(times):
            for ch in encode:
                result = result + chr(ord(ch) - key)
                result = ""
        key -= 1
        print result
    else:
        print "mode number not recognized"
    print result
    
#Example input:
ccipher()
