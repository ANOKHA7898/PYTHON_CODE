# check odd or even number between 1 to 100
num=int(input("Enter a Number: "))
if(num >= 1 and num <= 10**10):
    if(num%2==0):
        print(num,":is Even Number")
    elif(num%2==1):
        print(num,":is Odd Number")
else:
    print("Invalid input / larger Value")
