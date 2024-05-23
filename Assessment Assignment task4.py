# Is the number a prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 and 50 are: ")
for num in range(1, 51):
    if is_prime(num):
        print(num)
print()

# #Create a list of integers
numbers = list(range(1, 16))

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

