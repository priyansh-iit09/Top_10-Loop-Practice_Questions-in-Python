rows=5
for i in range(1,rows+1):
  for j in range(1,i+1):
    print("*",end=" ")
  print("")
# -----output-----
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


rows=5
for i in range(1,rows+1):
  for j in range(i):
    print(i,end=" ")
  print("")
# ---Output----
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 


rows=5
for i in range(1,rows+1):
  for j in range(i,rows+1):
    print("*",end=" ")
  print("")
#---Output----
# * * * * *
# * * * *
# * * *
# * *
# *


rows=5
for i in range(1,rows+1):#number3
  for j in range(1,i+1):
    print(j,end=" ")
  print("")
#---Output---
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 


rows=9
for i in range(1,rows+1,2):# number 6
  for j in range(1,i+1,2):
    print(i,end=" ")
  print("")
#---Output---
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9


rows=5
for i in range(1,rows+1): #number 5
  for j in range(i):
    print("*",end=" ")
  print("")
rows=4
for i in range(1,rows+1):
  for j in range(i-1,rows):
    print("*",end=" ")
  print("")
#---Output---
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


rows=4 
sum=1
for i in range(1,rows+1):
  for j in range(1,i+1):
       print(sum,end=" ")
       sum+=1
  print("")
#---Output---
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 


for i in range(1,5):
  for j in range(1,6):
    print(j,end=" ")
  print("")
#---Output---
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 


rows=7
for i in range(1,rows+1,2):
  for j in range(1,i+1,2):
    print(j,end=" ")
  print("")
#---Output---
# 1 
# 1 3 
# 1 3 5 
# 1 3 5 7 

rows=7
for i in range(1,rows+1):
  for j in range(1,i+1):
    print((i+1)-j,end=" ")
  print("")
#---Output---
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# 6 5 4 3 2 1 
# 7 6 5 4 3 2 1 