def factors(n):
    for i in range(1,1+n):
        if n%i==0:
            print(i,end=" ")

factors(12)            