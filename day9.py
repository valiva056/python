#the program to print true when the first and last element in the list was even, else print false.
num=[1,3,7,5,6,22]
if num[0]%2==0 and num[-1]%2==0:
    print("True")
else:
    print("False")
    
  
 #to create a function which performs the count method. Without using any methods.
d=[12,13,14,15,16,16,16,17]
s=[]
for i in d:
        if (i)==16:
            s.append(i)
print(s)    
print(len(s))


#to print the prime numbers in the new list from the existing list.
num=[1,2,3,4,5,6,7,8]
prime=[]
for i in range(0,len(num),1):
    number=num[i]
    fact=0
    for j in range(1,number+1,1):
     if number%j==0:
            fact+=1
    if fact==2:
        prime.append(number)
print(prime)                