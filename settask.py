#set methods
#Adding elements
# add()
s={1,2,3}
s.add(7)
print(s)
#update()
s={3,5,2,6}
s.update([9,7])
print(s)

#removing elements
#remove()
s.remove(3)
print(s)
#discard()
s.discard(9)
print(s)
#pop()
s.pop()
print(s)
#clear()
s.clear()
print(s)

#set operation
#union()
s1={1,5,2,6}
s2={6,3,9,8}
print({1,5,2,6}.union({6,3,9,8}))
#intersection()
print({1,5,2,6}.intersection({6,3,9,8}))
#difference()
print({1,5,2,6}.difference({6,3,9,8}))
#symmetric_difference()
print({1,5,2,6}.symmetric_difference({6,3,9,8}))

#sub set and super set methods
#issubset()
print({1,5,2,6}.issubset({6,3,9,8}))
#issuperset()
print({1,5,2,6}.issuperset({6,3,9,8}))
#isdisjoint()
print({1,5,2,6}.isdisjoint({6,3,9,8}))

#copy
s.copy()
print(s)


#Take a set of no,take elements from the user, remove that element  from the existing set  and store in the new set5

number={1,2,6,4,3,5,7,8,9}
new=set()
num=int(input("enter the number to remove"))
if num in number:
    number.remove(num)
    new.add(num)
print("remove element",new)     

#implementing the frozen set method on a set
u={1,2,34,5,6,}
v={5,3,6,7,2,9}   
print(v.isdisjoint(u))
print(v.issubset(u))
print(v.issuperset(u))
