p = float(input("Enter the principal amount: "))
n = int(input("Enter the number of years: "))
i = float(input("Enter the annual interest rate: "))
T = p * (1 + i/100) ** n
print("The total amount after", n, "years is:", T)