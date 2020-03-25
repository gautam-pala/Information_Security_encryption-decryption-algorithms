import numpy as np
import re
key=input("enter the key : ")
arr=np.zeros([6,6],dtype=str)
fe=key[0]
arr[0][0]=fe
j=0
k=1
for i in key:
    if i not in arr:
        arr[j][k]=i
        k=k+1
        if(k==6):
            j=j+1
            k=0
num=97
for l in range(26):
    if chr(num) not in arr:
         arr[j][k]=chr(num)
         num=num+1
         k=k+1
         if(k==6):
             j=j+1
             k=0
    else:
        num=num+1
for l in range(10):
    if str(l) not in arr:
         arr[j][k]=str(l)
         k=k+1
         if(k==6):
             j=j+1
             k=0
#print(arr)
f=open(r"C:\Users\Gautam Pala\Desktop\G1.txt","r")
f1=f.read()
getval=list([val for val in f1 if val.isalnum()])
result="".join(getval)
print(result)
f2=open("onlyallowed.txt","w")
f2.write(result)

arr2=[]
i1=[]
j1=[]
arr1=[result[i:i+2] for i in range(0,len(result),2)]
#print(arr1)
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        if(arr1[i][j] in arr and arr1[i][j+1] in arr):
            i1,j1=np.where(arr==arr1[i][j])
            i2,j2=np.where(arr==arr1[i][j+1])
            i3=i1[0]
            i4=i2[0]
            j3=j1[0]
            j4=j2[0]
            #print(i3,j3,i4,j4)
            if(i3==i4):
                if(j3==5):
                    arr2.append(arr[i3][0]+arr[i4][j4+1])
                elif(j4==5):
                    arr2.append(arr[i3][j3+1]+arr[i4][0])
                else:
                    arr2.append(arr[i3][j3+1]+arr[i4][j4+1])
            elif(j3==j4):
                if(i3==5):
                    arr2.append(arr[0][j3]+arr[i4+1][j4])
                if(j4==5):
                    arr2.append(arr[i3+1][j3]+arr[0][j4])
                else:
                    arr2.append(arr[i3+1][j3]+arr[i4+1][j4])
            else:
                arr2.append(arr[i3][j4]+arr[i4][j3])
        break
g1=[]
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        if(arr2[i][j] in arr and arr2[i][j+1] in arr):
            i5,j5=np.where(arr==arr2[i][j])
            i6,j6=np.where(arr==arr2[i][j+1])
            i7=i5[0]
            i8=i6[0]
            j7=j5[0]
            j8=j6[0]
            #print(i7,j7,i8,j8)
            if(i7==i8):
                if(j7==0):
                    g1.append(arr[i7][5]+arr[i8][j8-1])
                elif(j4==0):
                    g1.append(arr[i7][j7-1]+arr[i8][5])
                else:
                    g1.append(arr[i7][j7-1]+arr[i8][j8-1])
            elif(j7==j8):
                if(i7==0):
                    g1.append(arr[5][j7]+arr[i8-1][j8])
                if(j4==0):
                    g1.append(arr[i7-1][j7]+arr[5][j8])
                else:
                    g1.append(arr[i7-1][j7]+arr[i8-1][j8])
            else:
                g1.append(arr[i7][j8]+arr[i8][j7])
        break
    
print("plaintext : ",arr1)
print("keymatrix : ",arr)   
print("encrypted text : ",arr2)
print("after decryption : ",pt)
with open("final.txt","w") as f6:
    for i in g1:
        f6.write(i)
f7=open("final.txt","r")
#print(f7.read())  