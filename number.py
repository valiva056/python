# Print the prime digits in the given number
def  print_prime_digits(number):
    prime_digits={'2','3','4','5','7'}
    for digits in str(number):
        if digits in prime_digits:
            print(digits,end="")
num=int(input("enter a number:"))
print("print digits in the number:")
print_prime_digits(num)

# print the Armstrong number 
num=int(input("enter the number:"))
temp=num
temp2=num
length=0
while num!=0:
    num=num//10
    length+=1
    print(length)
    total_sum=0
    while temp!=0:
        last =temp%10
        total_sum=total_sum+last**length
        temp=temp//10
print(total_sum==temp2)
