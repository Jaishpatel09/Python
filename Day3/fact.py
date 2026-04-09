def factors(n):
    for i in range(1,1+n):
        if n%i==0:
            print(i,end=" ")
        return 10    
x=factors(12)
print(x)            