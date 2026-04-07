n=int(input("Enter n: "))
if n>1:
   for i in range (2,n):
      if(n%i==0):
         print(n,"Is Not a Prime Number")
         break
      else:
         print(n,"Is a Prime")
         