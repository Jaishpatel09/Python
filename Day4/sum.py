lst=[5,3,2,1,4,8]
lst_sum=0
for i in lst:
    lst_sum+=i

ans=[]
for i in lst:
    ans.append(lst_sum-i)

print(lst)    
print(ans)    