def print_integer_divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    print(divisors)

number = int(input("Enter a number: "))
print("Integer divisors:")
print_integer_divisors(number)