import re

def EE(r1, r2, flag = False):
    t1, t2, t = 0, 1, 0
    while r2 > 0:
        q = r1//r2
        r = r1 % r2
        r1, r2 = r2, r
        if flag:
            t = t1 - q * t2
            t1, t2 = t2, t

    if flag:
        return t1
    return r1

def encrypt():
    while 1:
        key1 = int(input("Enter key1:- "))
        if key1 < 26 and EE(26, key1) == 1:
            break
        print("{} should be in Z{}*".format(key1, 26))
    key2 = int(input("Enter key2:- ")) % 26

    f = open("plaintext.txt",'r').read()
    l = re.findall('[a-zA-Z]',f)
    f = "".join(l)
    fw = open("ciphertext.txt",'w')
    for char in f:
        x = ord(char.lower()) - 97
        x = (x * key1 + key2) % 26
        fw.write(chr(x + 97))
    fw.close()
    return key1, key2

def decrypt(key1, key2):
    key1 = EE(26, key1, True) % 26
    f = open("ciphertext.txt",'r').read()
    fw = open("decrypt.txt",'w')
    for char in f:
        x = ord(char) - 97
        x = ((x - key2) * key1) % 26
        fw.write(chr(x + 97))
    fw.close()


while(1):
	print("Enter\n1 - Encrypt\n2 - Decrypt\n")
	choice=int(input("Your choice? "))
	
	if(choice==1):
		key1, key2 = encrypt()
		break
	
	elif(choice==2):
		decrypt(key1, key2)
		break
		
	else:
		print("Enter Valid Choice\n")





