

students = []


def add_student():
    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    class_name = input("Enter class name: ")

    attended = int(input("Classes Attended: "))
    total = int(input("Total Classes: "))

    student = {
        "name": name,
        "id": student_id,
        "class" : class_name,
        "attended": attended,
        "total": total
    }

    students.append(student)
    print("Student record added successfully!\n")



def view_records():
    if len(students) == 0:
        print("No records found.\n")
        return

    print("\nAttendance Records")
    print("-" * 50)

    for student in students:
        print("Name:", student["name"])
        print("ID:", student["id"])
        print("Class name:", student["class name"])
        print("Classes Attended:", student["attended"])
        print("Total Classes:", student["total"])
        print("-" * 50)



def attendance_percentage(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100



def search_student():
    search_id = input("Enter Student ID to search: ")

    found = False

    for student in students:
        if student["id"] == search_id:
            percent = attendance_percentage(
                student["attended"],
                student["total"]
            )

            print("\nStudent Found")
            print("Name:", student["name"])
            print("Class name:", student["class name"])
            print("ID:", student["id"])
            print("Attendance Percentage:", round(percent, 2), "%")

            found = True
            break

    if not found:
        print("Student not found.\n")


def show_percentages():
    if len(students) == 0:
        print("No records available.\n")
        return

    for student in students:
        percent = attendance_percentage(
            student["attended"],
            student["total"]
        )

        print(student["name"], "-", round(percent, 2), "%")


def highest_attendance():
    if len(students) == 0:
        print("No records available.\n")
        return

    highest = students[0]
    highest_percent = attendance_percentage(
        highest["attended"],
        highest["total"]
    )

    for student in students:
        percent = attendance_percentage(
            student["attended"],
            student["total"]
        )

        if percent > highest_percent:
            highest = student
            highest_percent = percent

    print("\nHighest Attendance")
    print("Name:", highest["name"])
    print("Percentage:", round(highest_percent, 2), "%")


def lowest_attendance():
    if len(students) == 0:
        print("No records available.\n")
        return

    lowest = students[0]
    lowest_percent = attendance_percentage(
        lowest["attended"],
        lowest["total"]
    )

    for student in students:
        percent = attendance_percentage(
            student["attended"],
            student["total"]
        )

        if percent < lowest_percent:
            lowest = student
            lowest_percent = percent

    print("\nLowest Attendance")
    print("Name:", lowest["name"])
    print("Percentage:", round(lowest_percent, 2), "%")


while True:

    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student Attendance")
    print("2. View Attendance Records")
    print("3. Search Student ")
    print("4. Calculate Attendance Percentage")
    print("5. Show Highest Attendance")
    print("6. Show Lowest Attendance")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_student()

    elif choice == "4":
        show_percentages()

    elif choice == "5":
        highest_attendance()

    elif choice == "6":
        lowest_attendance()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")3
