def sum_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter a positive integer: "))  
if n > 0:
    result = sum_natural_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {result}")
else:
    print("Please enter a positive integer.")
