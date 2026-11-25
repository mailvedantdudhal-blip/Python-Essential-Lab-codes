num_students = int(input("Enter number of students in class: "))
total_class_score = 0
total_tests_count = 0

for i in range(1, num_students + 1):
    print(f"\n--- Student {i} ---")
    student_total = 0

    for t in range(1, 6):
        score = float(input(f"Enter score for test {t}: "))
        student_total += score

    student_avg = student_total / 5
    print(f"Student {i} Average Score: {student_avg:.2f}")

    total_class_score += student_total
    total_tests_count += 5

class_avg = total_class_score / total_tests_count
print(f"\nOverall Class Average: {class_avg:.2f}")
