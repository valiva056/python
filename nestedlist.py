#inding the max and min in nested list
l=[[1,2,3],[4,5,6],[7,8,9]]
final=[]
for sublist in l:
    largest=max(sublist)
    final.append(largest)
    print(final)
    
    
list=[[-1,-2,-3],[4,-6,3],[5,-6,-7]]
final=[]
for sublist in l:
    smallest=min(sublist)
    final.append(smallest)
    print(final)