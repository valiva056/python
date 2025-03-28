#Print the list of prime numbers and non prime numbers separately in given list.
numbers=[1,2,3,4,5,6,7,8,9,11]
prime_number=[]
non_prime_number=[]
for num in numbers:
    if num<2:
        non_prime_number.append(num)
    else:
        is_prime=True
        for i in range (2,int(num**0.5)+1):
            if num % i== 0:
              is_prime=False
            break
        if is_prime:
           prime_number.append(num)
        else:
            non_prime_number.append(num)
print("prime numbers:",prime_number)
print("non-prime numbers:",non_prime_number)    

#Count the skills through the dictionary.
this_list={
    "name":"valiva",
    "age":21,
    "student":"True",
    "skills":["python","java","react","html","js"],
    "language":["telugu","hindi","english"],
}
this_list["skills"].append("css")
print(len(this_list["skills"]))
