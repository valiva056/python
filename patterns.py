rows=int(input("enter the number of rows:"))
code=97
for r in range(1,rows+1):
    res=""
    for c in range(1,r+1):
        if r==rows or c==1 or c==r:
            res+=chr(code)+""
            code+=1
        else:
            res+=""+""
            code+=1
    print(res)