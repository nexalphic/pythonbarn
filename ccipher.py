letters = "abcdefghijklmnopqrstuvwxyz"
def ccipher(encode, key):
    crypted = ""
    if isalpha(encode) == True:
    	for ch in encode:
        	if isspace(ch) == False:
                if key > len(encode):
                    place = key - len(encode)
                else:
                    place = key
                
    	print crypted
    else:
        print "Error: alphabet letters only."
ccipher("hello", 3)
