#program to separate odd and even elementsfrom list
number=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
        print(even)
        print(odd)
        
        
#program to separate unique elements and add"*" at the end
data=[1,2,2,3,4,5,5,6,7] 
unique=[]
for n in data:
    if data.count(n)==1:
        unique.append(n)
        unique.append("*") 
        print(unique)      
        