rows=5
for i in range(rows):
    s=""
    for col in range(rows):
        s+=str(i+1)
        print(s)
        
rows=5
for i in range(rows):
    s=""
    for col in range(i+1):
        s+=str(i+1)
        print(s)        