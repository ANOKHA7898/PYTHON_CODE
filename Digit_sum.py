#python code to sum the 5 digit number

num= int(input("Enter Five Digit Number:"))
total_sum=0
temp = str(num)

if len(temp)>=5:
    print("Five digit Number: ",num)
    for i in range(len(temp)):
         total_sum = total_sum + num % 10
         num = num//10
    print("Total Sum Of Five Digit : ",total_sum)
    
else:
    print("Not Five Digit Number:",num)
