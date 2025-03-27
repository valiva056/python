#Print the list of prime numbers and non prime numbers separately in given list.
def is_prime(n):
    if n<2:
        return False 
    for i in range(2,int(n**0.5)+1):
      if n %i==0:
        return False
    return True
n=int(input("Enter a number:"))
count=0
num=n+1
while True:
    if not is_prime(num):
        num+=1
        continue
    count+=1
    if count==2:
        break
    num+=1
    if n<0:
        pass
    print("second prime after",n,"is:", num)


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
