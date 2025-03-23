#take a list of dictionary check whether that is eligible for vote or not and also check the citizen .
details=[{"name":"valiva",
    "age":20,
    "citizenship":"indian"},
{"name":"lavanya",
 "age":16,
 "citizenship":"indian"}]
for person in details:
  if person["age"]>19 and person["citizenship"]=="indian":
     person["eligible"]=True
  else:
    person["eligible"]=False
    print("wait for some time")
print(details)


# take a tupkeof elementes,print the unique elements in the new list
this_tuple=(1,3,5,6,2,7,2,9,1,2,3,4,9)
unique_list=list(set(this_tuple))
print(unique_list)
    
    
