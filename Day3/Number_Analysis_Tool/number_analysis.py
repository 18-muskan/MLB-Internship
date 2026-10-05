# Number Analysis Tool

print("=" * 40)
print("        NUMBER ANALYSIS TOOL")
print("=" * 40)

num = int(input("Enter a number: "))

print("\n" + "-" * 40)
print("              RESULTS")
print("-" * 40)


# Even or Odd

if num % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

print("Even / Odd       :", even_odd)


# Prime Check

if num < 2:
    prime = False
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    prime_result = "Prime"
else:
    prime_result = "Not Prime"

print("Prime Check      :", prime_result)


# Count Digits

digits = len(str(abs(num)))

print("Number of Digits :", digits)


# Reverse Number

reverse = str(abs(num))[::-1]

print("Reverse Number   :", reverse)


# Palindrome Check

if str(abs(num)) == reverse:
    palindrome = "Yes"
else:
    palindrome = "No"

print("Palindrome       :", palindrome)


print("-" * 40)
print("          ANALYSIS COMPLETED")
print("-" * 40)