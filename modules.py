#to print previous prime number to that number
original=34
num=original
for i in range(original-1,-1,-1):
    fact=0
    for j in range(2,i):
        if i%j==0:
            fact+=1
            break
        if fact==0:
            print(f"the previous prime is{i}")
            prev_prime=i
            break
        i=original+1
        while True:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    next_prime=i
                    print(f"the next prime is{i}")
                    break
                i+=1
                if nect_prime-original>original-prev_prime:
                    print(prev_prime,"is the nearest")
                elif original-prev_prime>next_prime-original:
                    print(next_prime,"is the nearest")
                else:
                    ("both are at equidistant")