# Python code to find the factorial of a Number

num = int(input("Enter a Number : "))

def Factorial(num):
    fact = 1

    if num >= 1:
        for i in range(1,num+1):
            fact *= i
    else:
        print("Invalid Input")

    print("The Factorial Of",num,"is :",fact)

Factorial(num)