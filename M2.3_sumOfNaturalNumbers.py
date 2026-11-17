num1 = int(input("Enter the first natural number: "))
num2 = int(input("Enter the second natural number: "))

if num1 > 0 and num2 > 0:
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}.")
else:
    print("Please enter natural numbers (positive integers greater than 0).")
