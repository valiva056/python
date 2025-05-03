#function to check whether a number is prime or not
def check_prime(num):
    count=0
    for i in range(1,num_1):
        if num%i==0:
            count+=1
            if count==2:
                return True
            else:
                return False
#function to find nth prime number
def nth_prime(n):
    prime_count=0
    num=1
    while prime_count<n:
        num+=1
        if check_prime(num):
            prime_count+=1
            return(num)
        num_1=int(input("enter first number:"))
        num_2=int(input("enter second number:"))
        print(nth_num(num_1))
        print(nth_num(num_2))            