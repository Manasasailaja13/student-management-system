#student-management-system

students = [
    [101, "Rahul", 20, "CSE", 85],
    [102, "Priya", 19, "ECE", 90],
    [103, "Kiran", 21, "IT", 88],
    [104, "Anjali", 20, "CSE", 95],
    [105, "Ravi", 22, "EEE", 80]
]

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # View Students
    if choice == 1:
        print("\nStudent Records")
        print("---------------------------------------------")
        print("ID\tName\tAge\tCourse\tMarks")
        print("---------------------------------------------")

        for student in students:
            print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", student[4])

    # Search Student
    elif choice == 2:
        sid = int(input("Enter Student ID: "))
        found = False

        for student in students:
            if student[0] == sid:
                print("\nStudent Found")
                print("ID     :", student[0])
                print("Name   :", student[1])
                print("Age    :", student[2])
                print("Course :", student[3])
                print("Marks  :", student[4])
                found = True
                break

        if found == False:
            print("Student Not Found")

    # Add Student
    elif choice == 3:
        sid = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))

        students.append([sid, name, age, course, marks])

        print("Student Added Successfully")

    # Update Student
    elif choice == 4:
        sid = int(input("Enter Student ID to Update: "))
        found = False

        for student in students:
            if student[0] == sid:
                student[1] = input("Enter New Name: ")
                student[2] = int(input("Enter New Age: "))
                student[3] = input("Enter New Course: ")
                student[4] = int(input("Enter New Marks: "))
                found = True
                print("Student Updated Successfully")
                break

        if found == False:
            print("Student Not Found")

    # Delete Student
    elif choice == 5:
        sid = int(input("Enter Student ID to Delete: "))
        found = False

        for student in students:
            if student[0] == sid:
                students.remove(student)
                found = True
                print("Student Deleted Successfully")
                break

        if found == False:
            print("Student Not Found")

    # Exit
    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")