# a = int(input("Enter your age :"))
# print("Your age is :",a)

# If-else statement

# if(a>18):
#     print("you can Drive")
# else:
#     print("you cannot Drive")


# elif-statement

# if(a<10):
#     print("You are child")
# elif(10<a and a<=17):
#     print("You are young")
# else:
#     print("You are Adult")    


# nested statement
a = int(input("Enter any number :"))
if(a == 0):
    print("Number is Zero")
elif(a>0):
    if(a<10):
        print("Number is between 1-10")
    elif(a>10 and a<=20):    
        print("Number is between 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Negative")            