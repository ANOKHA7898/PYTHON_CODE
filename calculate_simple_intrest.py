#This Python code is for calculating simple intrest

p_amt = float(input("Enter the Amount: "))
rate = float(input("Enter the rate per annum: "))
year = float(input("Enter the year: "))

si = (p_amt * rate * year )/100

print("Intrest is : ",si)

print("Total Amount : ",si + p_amt)