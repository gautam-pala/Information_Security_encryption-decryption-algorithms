import numpy as np

def encrypt():
	fr=open("plaintext.txt",'r')
    #f=fr.read()
    #f=str(f)
    #rint(f)
    f=fr.read() 
	while(1):
		depth=int(input("Enter depth:- "))
		print(depth)
		if(depth<len(f)):
			break
	a=np.empty((depth,len(f)),dtype="str")
	a[:]='-'
	(row,col,factor)=(0,0,1)
	for char in f:
		a[row,col]=char
		row+=factor
		col+=1
		if(row==0 or row==depth-1):
			factor*=-1
		
	print(a)
	fw=open("ciphertext.txt",'w')
	for i in range(depth):
		for j in range(len(f)):
			if(a[i,j]!='-'):
				fw.write(a[i,j])
	fw.close()

def decrypt():
	fr=open("ciphertext.txt",'r')
	f=fr.read()
	while(1):
		depth=int(input("Enter depth:- "))
		print(depth)
		if(depth<len(f)):
			break
	a=np.empty((depth,len(f)),dtype="str")
	a[:]='-'
	(row,col,factor,n)=(0,0,1,0)
	for i in range(len(f)):
		a[row,col]='@'
		row+=factor
		col+=1
		if(row==0 or row==depth-1):
			factor*=-1
	
	for i in range(depth):
		for j in range(len(f)):
			if(a[i,j]=='@'):
				a[i,j]=f[n]
				n+=1

	print(a)
	fw=open("deciphertext.txt",'w')
	(row,col,factor)=(0,0,1)	
	for i in range(len(f)):
		fw.write(a[row,col])
		row+=factor
		col+=1
		if(row==0 or row==depth-1):
			factor*=-1
	fw.close()		

while(1):
	print("Enter\n1 - Encrypt\n2 - Decrypt\n")
	choice=int(input("Your choice? "))
	
	if(choice==1):
		encrypt()
		break
	
	elif(choice==2):
		decrypt()
		break
		
	else:
		print("Enter Valid Choice\n")
