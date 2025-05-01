#write a program to print the count of number of fibonocii numbers in between 0 to 500
a,b=0,1
count=0
for i in range(100):
    if a>500:
        break
    print(a,end='')
    count+=1
    a,b=b,a+b
    print("fibonocci numbers",count)