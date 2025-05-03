# lcm of 3 numbers
a=30
b=54
c=34
lcm=max(a,b,c)
while True:
    if lcm%a==0 and lcm%b==0 and lcm%c==0:
        break
    lcm+=1
    print(lcm)