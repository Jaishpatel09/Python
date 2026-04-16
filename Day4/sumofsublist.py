lst=[[1,3,5,6],[3,4,5],[3,5,7],[10,20,30]]

ans=[]
for i in range(len(lst)):
    temp=0
    for j in lst[i]:
        temp+=j
    ans.append(temp)
print(ans)    