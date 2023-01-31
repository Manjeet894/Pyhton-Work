
num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
num3 = int(input("Enter the 3rd number"))


if(num1>num2) and (num1>num3):
    print(num1," First Number is greater ")
elif(num2>num1) and (num2>num3):
    print(num2,"2nd Number is greater")
else:
    print(num3,"3rd Number is greater")      

