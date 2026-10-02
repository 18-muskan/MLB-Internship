# Task 1: Find the largest number in a list

numbers = [10, 25, 7, 40, 15]

largest = max(numbers)

print("Largest number:", largest)


# Task 2: Find the second largest number

numbers = [10, 25, 7, 40, 15]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("Second largest number:", second_largest)


# Task 3: Remove duplicate values from a list

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print("List without duplicates:", unique_numbers)


# Task 4: Reverse a list without using reverse()

numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("Reversed list:", reversed_list)


# Task 5: Find common elements between two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = list(set(list1) & set(list2))

print("Common elements:", common)