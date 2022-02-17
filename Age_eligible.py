def Age_eligible(num):


    if num < 18:

        print(" Sorry You are Minor and not eligible for work")

    elif num in range(18,60):

        print(" Congrats You are Eligible to work")

    elif num > 60:
               
        print("your not eligible to work.\n--Take Rest--")
        

age = input("Enter your age:")

print("your entered age:",age)

try:

    Age_eligible(int(age))

except ValueError:

    print(" entered value not convert in to integer. \n-->enter your age in numbers'ex:23 45 64")




