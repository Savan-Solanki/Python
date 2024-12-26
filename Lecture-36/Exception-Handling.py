# Exception Handling is used for find error in code

a = input("Enter the number : ")
print(f"Multi. table of {a}is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}") 
except Exception as e:
    print(e)         

print("Some imp code")        
print("End Program")        