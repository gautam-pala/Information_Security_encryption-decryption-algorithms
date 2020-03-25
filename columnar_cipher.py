import numpy as np
import math
plaintext=input("enter the plaintext")
key=input("enter the key")
key_length=len(key)
lop=len(plaintext)
row=math.ceil(lop/key_length)
print(row)
print(lop)
arr=np.zeros([row,key_length],dtype=str)
arr1=[]
dicts={}
temp=[]
darr=np.zeros([row,key_length],dtype=str)
arr3=np.zeros([row,key_length],dtype=str)
for i in range(97,123):
    arr1.append(chr(i))
for i in range(26):
    dicts[i]=arr1[i]
print(dicts)
print(len(dicts))
print(arr1)
for i in key:
    for j in dicts:
        if(i==dicts[j]):
            temp.append(j)
print(temp)
k=0
for i in range(row):
    for j in range(key_length):
        arr[i][j]=plaintext[k]
        k=k+1
        if(k>=lop):
            break
arr2=np.zeros(len(temp),dtype=int)
a=0
arr4=[]
for i in range(len(temp)):
    low=min(temp)
    index=temp.index(low)
    arr4.append(low)
    arr2[index]=a
    a=a+1
    temp[index]=9999
    

 
print(arr)
print()
print(arr2)
b=0
for i in arr2:
    for j in range(row):
        arr3[j][b]=arr[j][i]
    b=b+1
c=0
for i in arr2:
    for j in range(row):
        darr[j][i]=arr3[j][c]
    c=c+1
print(arr3)
print()
print(darr)