# python code to check a number is prime or not

def chk_Prime(num):

    if num <=1:
        print("Not Prime Number")

    elif num > 3:
        for i in range(2,num//2):
            if num % i == 0:
                print("Not Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Prime Number")

        

for i in range(5):
    num = int(input("Enter the Number: "))
    chk_Prime(num)