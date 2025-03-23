#take the input number from user and
num=int(input("enter the number"))
print("factor of num")
for i in range(1,num+1):
    if num%i==0:
        print(i)
        
 #print tables from 1-5 with multiplying of even numbers       
num=int(input("enter the number"))
print("factor of num")
for i in range(1,6):
    for j in range(2,11,2):
         print(i,"x",j,"=",i*j)