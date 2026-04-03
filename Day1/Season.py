month=int(input("Enter Month: "))
if month in (3,4,5):
    print("Summer")
elif month in (6,7):
    print("Rain")
elif month in (8,9):
    print("Spring")
elif month in (10,11,12,1,2):
    print("Winter")
else:
    print("Invalid Month")