# Ask for the number of students
num_students = int(input("Enter the number of students: "))

# List to hold each student's details (name, scores, average, grade)
student_data = []

# Collect data for each student
for i in range(num_students):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Enter student name: ")

    # Input the scores as comma-separated values, then convert to a list of integers
    scores = list(map(int, input("Enter scores for 3 subjects (comma-separated): ").split(',')))

    # Calculate the average score
    average_score = sum(scores) / len(scores)

    # Determine the grade based on the average score
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    else:
        grade = 'D'

    # Store the student's details in a tuple and append to the list
    student_data.append((name, scores, average_score, grade))

# Output the results
print("\nSummary of Students:")
for student in student_data:
    name, scores, average_score, grade = student
    print(f"{name}'s scores: {scores} | Average: {average_score:.2f} | Grade: {grade}")
