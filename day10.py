#count method on a list by making input user without using actual method

number=[1,2,3,4,4,6,6,6,7,8,6,6]
ele=6
count=0
for i in range(len(number)):
    if number[i]==ele:
        count+=1
        print(count)
        
        
 #copy method on a list just as the above condition       
my_list=[1,2,"apple",[1,2],False]
res=[]
for i in range(len(my_list)):
    res.append(my_list[i])
    print(res)