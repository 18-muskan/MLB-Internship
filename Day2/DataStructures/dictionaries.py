# Task 10: Create a student record dictionary

student = {
    "name": "Muskan",
    "age": 21,
    "course": "AI & ML",
    "marks": 85
}

print("Student Record:")
print(student)


# Task 11: Calculate average marks of students

marks = {
    "Ali": 80,
    "Sara": 90,
    "Muskan": 85
}

average = sum(marks.values()) / len(marks)

print("Average marks:", average)


# Task 12: Count frequency of words in a sentence

sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)