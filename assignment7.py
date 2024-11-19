# for user input
name = input("Enter your Name: ")

# for fav number input 
num1 = int(input("Enter your 1st fav number: "))
num2 = int(input("Enter your 2nd fav number: "))
num3 = int(input("Enter your 3rd fav number: "))

# print number inout
print(f"\nHello, {name}!, Let's explore your fav numbers: ")

# number in the list
numbers = [num1, num2, num3]

# for verify number is even or odd
for num in numbers:
    if num % 2 == 0:
        print(f"The number '{num}' is even. ")
    else:
        print(f"The number '{num}' is odd. ")

# for print tuple of number and its square 
for num in numbers:
    print(f"The number {num} and square of number: ({num}, {num ** 2})")

# for sum of number
sum = sum(numbers)
print(f"\nAmazing! The sum of your fav number is: {sum}")

# for check prime number
if sum <= 1:
    print(f"{sum} is not a prime")
else:
    is_prime = True
    for number in range(2, int(sum ** 0.5) + 1):
        if sum % number == 0:
            is_prime = False
            break

    if is_prime:
        print(f"\nWow, {sum} is a prime number!")
    else:
        print(f"\n{sum} is not a prime number, but that's okay!")