# Student Grade Evaluator (Easy Version)

def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

students = {}

while True:
    name = input("Enter student name: ")
    mrk1 = float(input("Enter mark 1: "))
    mrk2 = float(input("Enter mark 2: "))
    mrk3 = float(input("Enter mark 3: "))

    avg = (mrk1 + mrk2 + mrk3) / 3
    grade = get_grade(avg)

    students[name] = {"Average": avg, "Grade": grade}

    again = input("Add another student? (yes/no): ").lower()
    if again != "yes":
        break

# Save results to file
with open("students.txt", "w") as f:
    for name, info in students.items():
        f.write(f"{name} - Average: {info['Average']:.2f}, Grade: {info['Grade']}\n")

print("\nResults saved to students.txt ")