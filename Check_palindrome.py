# this python code is to check the entered number is palindrome or not


num = int(input("Enter a Number: ")) #taking input from the user
temp_num = num
rev = 0                              # intial value of reverseing number

#logic of the program
while num > 0:
    rev = rev * 10 + (num %10)
    num = num // 10

print("The Reverse of the number is: ", rev)

if rev == temp_num:
    print("Entered Number : ",temp_num,"is Palindrome")
else:
    print("Entered Number : ",temp_num,"is Not Palindrome")
