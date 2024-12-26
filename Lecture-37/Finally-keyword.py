try:
    l = [2,4,5,8]
    i = int(input("Enter Index: "))
    print(l[i])

except:
    print("Some Error in Code")

finally:
    print("i am always run")