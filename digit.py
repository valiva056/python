 #Task1 Take 9 digit number,take one digit check whether that digit is present or not , print the count of that digit and positions

number=input("enter 9-digit number")
digit=input("enter a single digit to serch:")
count=0
position=[]
for i in range(len(number)):
    if number[i]==digit:
        count+=1
        position.append(i)
        if count>0:
            print("{} food {} count times at position {}".format(digit,count,position))
        else:
            print("not found")
#Task2: Take a number check whether that no is in descending order or not
num=98776
prev=num%10
num=num//10
is_desc=True
while num!=0:
    digit=num%10
    print(prev,digit)
    if prev>digit:
        is_desc=False
        break
    prev=digit
    num=num//10
    if is_desc:
        print("descending order:")
    else:
        print("not descending order:")