# Problem 11: Reverse a number

num = input("Enter a number: ")

reverse = num[::-1]

print("Reverse:", reverse)


# Problem 12: Check palindrome

num = input("Enter a number: ")

reverse = num[::-1]

if num == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# Problem 13: Fibonacci sequence

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)

    next_num = a + b
    a = b
    b = next_num


# Problem 14: Check prime number

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")


# Problem 15: Prime numbers from 1 to 100

for num in range(2, 101):

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)