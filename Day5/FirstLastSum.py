lst1=[[23,45,76],[45,3,12],[3,5,20]]
lst2=[]
for i in lst1:
    lst2.append(i[0])
    lst2.append(i[-1])
print(lst2)