#Student grade manager
import json

students = []

# Load student data from file
def load_data():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save student data to file
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=3) #indent is used to make it look readable on the file

# Add a new student
def add_student():
    name = input("Enter student name: ")
    student = {"name": name, "grades": {}}
    students.append(student)
    print(f"{name} has been added.")

# Add grades to a student
def add_grades():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            while True:
                subject = input("Enter subject (or type 'done' to finish): ")
                if subject.lower() == "done":
                    break
                try:
                    score = float(input(f"Enter score for {subject}: "))
                    student["grades"][subject] = score
                except ValueError:
                    print("Invalid score. Please enter a number.")
            print("Grades added successfully.")
            return
    print("Student not found.")

# Calculate GPA
def calculate_gpa():
    name = input("Enter student name to calculate GPA: ")
    for student in students:
        if student["name"].lower() == name.lower():
            grades = student["grades"].values()
            if grades:
                gpa = sum(grades) / len(grades)
                print(f"{name}'s GPA is: {round(gpa, 2)}")
            else:
                print("No grades found.")
            return
    print("Student not found.")

# View all students
def view_students():
    if not students:
        print("No students yet.")
        return

    for student in students:
        print(f"\nName: {student['name']}")
        if student["grades"]:
            for subject, grade in student["grades"].items():
                print(f"  {subject}: {grade}")
        else:
            print("  No grades yet.")

# Main menu
def main():
    global students
    students = load_data()

    while True:
        print("\n Student Grades Manager")
        print("1. Add Student")
        print("2. Add Grades")
        print("3. Calculate GPA")
        print("4. View All Students")
        print("5. Save and Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grades()
        elif choice == "3":
            calculate_gpa()
        elif choice == "4":
            view_students()
        elif choice == "5":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()

