a = int(input("Enter value bett. 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("value should be bett. 5 and 9")

print(a)