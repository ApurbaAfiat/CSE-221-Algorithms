# -*- coding: utf-8 -*-
"""CSE221_LAB02_Task-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1czHE4JaO1LSihiJoEbTSOY3l0vavGaJS
"""

file_input=open("/content/Input4.txt","r")
file_output=open("/content/Output4.txt","w")
list_1=file_input.readline().split()
n=int(list_1[0])
p=int(list_1[1])
list_2=[]
for i in range(n):
  x=file_input.readline().split()
  list_2.append([int(x[0]),int(x[1])])
for i in range(n):
  for j in range(i+1,n):
    if list_2[j][0]<list_2[i][0]:
      list_2[j],list_2[i]=list_2[i],list_2[j]

c1=0
l3=[]
k=0
while k<p:
  x=0
  j=0
  while j<n:
      for i in list_2:
        if i[0]>=x:
          c1+=1
          l3.append(i)
          x=i[1]
          list_2.remove(i)
      j+=1
  k+=1
file_output.write(str(c1))
file_output.close()