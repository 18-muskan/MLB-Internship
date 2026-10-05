# Problem 6: Print numbers from 1 to 100

for i in range(1, 101):
    print(i)


# Problem 7: Print even numbers from 1 to 100

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# Problem 8: Find sum of numbers from 1 to N

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# Problem 9: Multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Problem 10: Count digits in a number

num = input("Enter a number: ")

print("Number of digits:", len(num))