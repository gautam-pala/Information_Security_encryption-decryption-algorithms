def enc(key):
	f= open("plain_text.txt","r")
	f2 = open("encr_text.txt","w")

	for line in f:
		for char in line:
			ch = chr((ord(char)+key)%256)
			f2.write(ch)

def dec(key):
	f= open("plain_text.txt","w")
	f2 = open("encr_text.txt","r")
	for line in f2:
		for char in line:
			ch = chr((ord(char)-key)%256)
			f.write(ch)



choice = 1

while(choice == 1 or choice == 2):
	print("1) Encrypt the plain text")
	print("2) Decrypt the plain text")

	choice = int(input("Please Choose from below : "))
	

	if(choice == 1):
		key = input("Please enter the key : ")
		enc(key)
		break

	elif(choice == 2):
		print("Select the method : ")
		print("1)Brute Force\n2)With the perticuler key\n3)With Crypt Analysis")
		d_c = int(input("Selct your method : "))

		if(d_c == 1):
			for key in range(1,256):
				f= open("plain_text.txt","w")
				f2 = open("encr_text.txt","r")
				for line in f2:
					for char in line:
						ch = chr((ord(char)-key)%256)
						f.write(ch)
				f.close()
				f= open("plain_text.txt","r")
				file = f.read()
				print(file)
				f.close()
				print("Is the output okay???(0/1)")
				d = input()
				if(d == 1):
					print("The key : ",key)
					break
				f2.seek(0,0)

		elif(d_c == 3):
			priority_list = [' ','e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']
			dict = {}
			f = open("encr_text.txt","r")
			for line in f:
				for char in line:
					if char in dict.keys():
						dict[char]+=1

					else:
						dict[char] = 1
			f.close()
			max = 0
			max_c = ['q']
			for i in dict.keys():
				if max < dict[i]:
					max = dict[i]
					max_c[0] = i
					
			max_char = max_c[0]
			print (max_char)

			
			for i in range(len(priority_list)):
				key = ord(max_char)-ord(priority_list[i])
				print(key)

				f= open("plain_text.txt","w")
				f2 = open("encr_text.txt","r")
				for line in f2:
					for char in line:
						ch = chr((ord(char)-key)%256)
						f.write(ch)
				f.close()
				f= open("plain_text.txt","r")
				file = f.read()
				print(file)
				f.close()
				print("Is the output okay???(0/1)")
				d = input()
				if(d == 1):
					print("The key : ",key)
					break
				f2.seek(0,0)
				
		else:
			key = input("Please enter the key : ")
			dec(key)
			break

	else:
		print("Please enter the valid choice")

