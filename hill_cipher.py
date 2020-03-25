charset = "abcdefghijklmnopqurstuvwxyz"
import math
import sys
import copy



def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y



def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None
	else:
		return x % m



def determinant(A):
    n = len(A)
    AM = copy.deepcopy(A)
 
    for fd in range(n):
        for i in range(fd+1,n):
            if AM[fd][fd] == 0: 
                AM[fd][fd] = 1.0e-18
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
     
    product = 1.0
    for i in range(n):
        product *= AM[i][i] 
 
    return product



def generateKeyMatrix(key,n):
	k = 0
	z = 0
	if(len(key) != n*n):
		while(len(key) != n*n):
			key+= charset[z]
			z+=1


	for i in range(n):
		for j in range(n):
			if(key[k].lower() in charset):
				Key_Matrix[i][j] = ord(key[k].lower())%97
				k+=1
			else:
				k+=1



def generateMessageArray(filename,n):
	file = open(filename,"r")

	for line in file:
		for char in line:
			if char.lower() in charset:
				Message.append(char.lower())

	file.close()

	if(len(Message)%n != 0):
		for i in range(len(Message)%n):
			Message.append("z")



def generateMessageVector(n,index):
	for i in range(n):
		Message_Vector[i][0] = ord(Message[index])%97
		index+=1

	return index


def encrypt(Message_Vector,n): 
    for i in range(n): 
        for j in range(1): 
            Cipher_Vector[i][j] = 0
            for x in range(n): 
                Cipher_Vector[i][j] += (Key_Matrix[i][x] * 
                                       Message_Vector[x][j]) 
            Cipher_Vector[i][j] = Cipher_Vector[i][j] % 26

            Encryption.append(chr(Cipher_Vector[i][j] + 97))


def transposeMatrix(m):
    return list(map(list,zip(*m)))


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixInverse(n, inv_multiplyer):
    if (n == 2):
        return [[Key_Matrix[1][1]*inv_multiplyer, -1*Key_Matrix[0][1]*inv_multiplyer],
                [-1*Key_Matrix*m[1][0]*inv_multiplyer, Key_matrix*[0][0]*inv_multiplyer]]

    cofactors = []
    for r in range(n):
        cofactorRow = []
        for c in range(n):
            minor = getMatrixMinor(Key_Matrix,r,c)
            cofactorRow.append(((-1)**(r+c)) * round(determinant(minor)))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = ((cofactors[r][c]*inv_multiplyer) % 26)
    return cofactors


def decrypt(Message_Vector, n):
	for i in range(n): 
		for j in range(1): 
			Plain_Vector[i][j] = 0
			for x in range(n): 
				Plain_Vector[i][j] += (Inverse_Matrix[i][x] * Message_Vector[x][j]) 
			Plain_Vector[i][j] = Plain_Vector[i][j] % 26
			print(Plain_Vector)
			Decryption.append(chr(Plain_Vector[i][j] + 97))




choice = input("Encryption or Decryption : ")
key = input("Enter the key : ")
n = math.ceil(math.sqrt(len(key)))


index = 0
Message = []
Encryption = []
Decryption = []
Key_Matrix = [[0] * n for i in range(n)]
Inverse_Matrix = [[0] * n for i in range(n)]
Message_Vector = [[0] for i in range(n)]
Cipher_Vector = [[0] for i in range(n)]
Plain_Vector = [[0] for i in range(n)]


if(choice == "Encryption"):
	filename = input("Enter the Plain text filename : ")

	generateKeyMatrix(key,n)

	if(modinv(round(determinant(Key_Matrix)),26) == None):
		print("Key is not feasible... Please try Again!!!")
		sys.exit()

	
	generateMessageArray(filename, n)


	while(index != len(Message)):
		index = generateMessageVector(n, index)
		encrypt(Message_Vector, n)

	string = "".join(Encryption)

	file = open("encr_text.txt","w")
	file.write(string)
	file.close()



elif(choice == "Decryption"):
	filename = input("Enter the Decrypted text filename : ")

	generateKeyMatrix(key, n)
	inv_multiplyer = modinv(round(determinant(Key_Matrix)),26)
	Inverse_Matrix = getMatrixInverse(n, inv_multiplyer)

	print(Inverse_Matrix)

	generateMessageArray("encr_text.txt", n)

	while(index != len(Message)):
		index = generateMessageVector(n, index)
		decrypt(Message_Vector, n)

		
	string = "".join(Decryption)

	file = open(filename,"w")
	file.write(string)
	file.close()
	

